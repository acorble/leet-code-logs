#!/usr/bin/env python3
"""同じ問題を解き直したときに、前回のコードを attempts/ に退避する。

現在の solution.py を attempts/<日付>.py へ移し、README の復習ログに行を追加する。
退避後の solution.py には前回のコードが残っているので、今回の解答で上書きする。

使い方:
    python scripts/new_attempt.py 1
    python scripts/new_attempt.py 1 --result AC --minutes 8 --note "今回はヒント無しで解けた"
"""

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
START = "<!-- ATTEMPTS:START -->"
END = "<!-- ATTEMPTS:END -->"


def find_problem(target: str) -> Path:
    """問題番号またはパスから問題ディレクトリを探す。"""
    path = Path(target)
    if path.is_dir():
        return path.resolve()

    if target.isdigit():
        prefix = f"{int(target):04d}-"
        hits = sorted(p for p in PROBLEMS.glob("*/*") if p.is_dir() and p.name.startswith(prefix))
    else:
        hits = sorted(p for p in PROBLEMS.glob("*/*") if p.is_dir() and target in p.name)

    if not hits:
        sys.exit(f"問題が見つかりません: {target}")
    if len(hits) > 1:
        listing = "\n".join(f"  {p.relative_to(ROOT)}" for p in hits)
        sys.exit(f"複数の問題に一致しました。パスで指定してください:\n{listing}")
    return hits[0]


def previous_day(readme: Path, fallback: str) -> str:
    """退避しようとしている solution.py が、いつ書かれたものかを復習ログから取る。

    退避先のファイル名は「そのコードを書いた日」でなければ意味がないので、
    今回の日付ではなく、solution.py を指している行の日付を使う。
    """
    text = readme.read_text(encoding="utf-8") if readme.exists() else ""
    block = re.search(r"<!-- ATTEMPTS:START -->(.*?)<!-- ATTEMPTS:END -->", text, re.DOTALL)
    if block:
        rows = re.findall(
            r"^\|\s*\d+\s*\|\s*([^|]*?)\s*\|.*?\[solution\.py\]",
            block.group(1),
            re.MULTILINE,
        )
        if rows and rows[-1]:
            return rows[-1]
    m = re.search(r"^- 初回: (.*)$", text, re.MULTILINE)
    return m.group(1).strip() if m else fallback


def archive_path(attempts_dir: Path, day: str) -> Path:
    """同じ日に複数回解いた場合は -2, -3 と連番を付ける。"""
    candidate = attempts_dir / f"{day}.py"
    n = 2
    while candidate.exists():
        candidate = attempts_dir / f"{day}-{n}.py"
        n += 1
    return candidate


def update_log(readme: Path, archived_rel: str, day: str, result: str, minutes: str, note: str) -> int:
    """既存行の solution.py リンクを退避先に貼り替え、新しい回の行を追加する。"""
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit(f"{readme.name} に {START} / {END} のマーカーがありません。手で追加してください。")

    block = re.search(rf"{re.escape(START)}(.*?){re.escape(END)}", text, re.DOTALL).group(1)
    block = block.replace("[solution.py](solution.py)", f"[{archived_rel}]({archived_rel})")

    lines = [ln for ln in block.strip().splitlines() if ln.strip()]
    attempt_no = sum(1 for ln in lines if re.match(r"^\|\s*\d+\s*\|", ln)) + 1
    row = (
        f"| {attempt_no} | {day} | {result or '-'} | {minutes or '-'} "
        f"| [solution.py](solution.py) | {note} |"
    )
    new_block = "\n\n" + "\n".join(lines + [row]) + "\n\n"

    text = re.sub(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        START + new_block + END,
        text,
        flags=re.DOTALL,
    )
    readme.write_text(text, encoding="utf-8")
    return attempt_no


def add_thoughts_heading(readme: Path, attempt_no: int) -> None:
    """「考えたこと / アプローチ」に空の「### N 回目」見出しだけを足す。

    中身は本人が手で書く欄なので、見出し以外は一切触らない。
    """
    text = readme.read_text(encoding="utf-8")
    heading = "## 考えたこと / アプローチ"
    start = text.find(heading)
    if start == -1:
        return

    end = text.find("\n## ", start + len(heading))
    end = len(text) if end == -1 else end

    section = text[start:end].rstrip()
    if re.search(rf"^### {attempt_no} 回目\s*$", section, re.MULTILINE):
        return

    section += f"\n\n### {attempt_no} 回目\n"
    readme.write_text(text[:start] + section + text[end:], encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="解き直しの記録を始める")
    parser.add_argument("problem", help="問題番号 (例: 1)、スラッグの一部、または問題ディレクトリのパス")
    parser.add_argument("-r", "--result", default="", help="結果 (AC / WA / TLE / giveup など)")
    parser.add_argument("-m", "--minutes", default="", help="かかった時間 (例: 12分)")
    parser.add_argument("-n", "--note", default="", help="今回のひとことメモ")
    parser.add_argument("--date", default="", help="解いた日 (省略時は今日。例: 2026-07-11)")
    args = parser.parse_args()

    problem = find_problem(args.problem)
    solution = problem / "solution.py"
    if not solution.exists():
        sys.exit(f"solution.py がありません: {problem.relative_to(ROOT)}")

    readme = problem / "README.md"
    attempts = problem / "attempts"
    attempts.mkdir(exist_ok=True)
    day = args.date or date.today().isoformat()

    # 退避先の名前は「今回の日付」ではなく「退避するコードを書いた日」
    dest = archive_path(attempts, previous_day(readme, day))
    shutil.copy2(solution, dest)

    rel = dest.relative_to(problem).as_posix()
    no = update_log(readme, rel, day, args.result, args.minutes, args.note)
    add_thoughts_heading(readme, no)

    print(f"{problem.relative_to(ROOT)} — {no} 回目の記録を開始しました")
    print(f"  前回のコードを退避: {rel}")
    print(f"  今回の解答は solution.py を上書きして書く")
    print(f"  README に「### {no} 回目」の見出しを用意しました（中身は自分で書く）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
