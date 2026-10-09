"""復習ログから「次にいつ解き直すか」を決めるための共通処理。

考え方は忘却曲線に基づく間隔反復。何も見ずに解けるたびに次までの間隔を広げ、
ヒントや過去の解答を見たら短く戻す。

  自力  意味                              次の段階
  ◎    何も見ずにすんなり解けた           1 段上げる
  ○    何も見ずに解けたが時間がかかった   据え置き（最低 1 段目 = 1 週間）
  △    ヒント・過去の解答・解説を見た     0 段目（3 日）に戻す
  ×    解けなかった                       0 段目（3 日）に戻す
  ?    記録なし                           ○ と同じに扱う
  -    同日の書き直し                     数えない

同じ日の 2 回目以降は「直後の書き直し」で思い出す練習になっていないので数えない。
"""

import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

INTERVALS = [3, 7, 14, 30, 60]  # 段階ごとの日数。最後の段で ◎ を取ったら卒業
RECALL_MARKS = {"◎", "○", "△", "×"}

ATTEMPTS_RE = re.compile(r"<!-- ATTEMPTS:START -->(.*?)<!-- ATTEMPTS:END -->", re.DOTALL)
NEXT_HEADING = "## 次回やること"


def _cells(line: str) -> list:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_attempts(text: str) -> list:
    """復習ログの表を、見出しをキーにした dict のリストにする。"""
    block = ATTEMPTS_RE.search(text)
    if not block:
        return []
    lines = [ln for ln in block.group(1).splitlines() if ln.strip().startswith("|")]
    if not lines:
        return []
    header = _cells(lines[0])
    rows = []
    for ln in lines[1:]:
        cells = _cells(ln)
        if cells and cells[0].isdigit():
            rows.append(dict(zip(header, cells)))
    return rows


def parse_next_steps(text: str) -> list:
    """「## 次回やること」の未完了の箇条書きを返す。[x] が付いたものは除く。"""
    start = text.find(NEXT_HEADING)
    if start == -1:
        return []
    end = text.find("\n## ", start + len(NEXT_HEADING))
    section = text[start + len(NEXT_HEADING):end if end != -1 else len(text)]
    section = re.sub(r"<!--.*?-->", "", section, flags=re.DOTALL)
    items = []
    for line in section.splitlines():
        m = re.match(r"^\s*[-*]\s+(\[([ xX])\]\s*)?(.+?)\s*$", line)
        if m and (m.group(2) or " ") == " ":
            items.append(m.group(3))
    return items


def recall_of(row: dict) -> str:
    mark = row.get("自力", "").strip()
    if mark in RECALL_MARKS or mark == "-":
        return mark
    if row.get("結果", "").strip().lower() == "giveup":
        return "×"
    return "?"


def _to_date(s: str):
    try:
        return date.fromisoformat(s.strip())
    except ValueError:
        return None


@dataclass
class Schedule:
    level: int = 0
    history: list = field(default_factory=list)  # 数えた回の自力の記号
    last: date | None = None

    @property
    def graduated(self) -> bool:
        return self.level >= len(INTERVALS)

    @property
    def interval(self) -> int | None:
        return None if self.graduated else INTERVALS[self.level]

    @property
    def due(self) -> date | None:
        if self.last is None or self.graduated:
            return None
        return self.last + timedelta(days=self.interval)


def schedule(rows: list) -> Schedule:
    s = Schedule()
    prev_day = None
    for row in rows:
        day = _to_date(row.get("日付", ""))
        if day is None:
            continue
        mark = recall_of(row)
        s.last = day
        if day == prev_day or mark == "-":
            continue
        prev_day = day
        s.history.append(mark)
        if mark == "◎":
            s.level += 1
        elif mark in ("○", "?"):
            s.level = max(s.level, 1)
        else:  # △ ×
            s.level = 0
    return s


def load(readme: Path) -> tuple:
    text = readme.read_text(encoding="utf-8") if readme.exists() else ""
    return schedule(parse_attempts(text)), parse_next_steps(text)
