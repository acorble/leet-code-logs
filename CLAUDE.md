# leet-code-logs

LeetCode で解いた問題のコードと考えを記録するリポジトリ。

## 前提

- Python。仮想環境は `.venv`（`./.venv/bin/python -m pytest` で実行する。
  Windows では `./.venv/Scripts/python.exe`）
- 問題は `problems/<category>/<4桁番号>-<スラッグ>/` に 1 問 1 ディレクトリ
- `solution.py` は常に最新の解答。過去の解答は `attempts/<日付>.py` に残す
- 同じ問題を何度も解き直して記録するのが前提。**過去の解答とメモを消さないこと**
- 昔 Java で解いた回は、Python に訳さず `attempts/<日付>.java` にそのまま置き、復習ログからリンクする。
  Python でまだ解いていない問題の `solution.py` は `NotImplementedError` の雛形のままにし、
  テストは Python の解答が入るまでスキップする（例: `problems/arrays-hashing/0242-valid-anagram`）。
  `new_attempt.py` は、復習ログに `solution.py` の回がなければ退避せずに次の回を足す
- カテゴリは以下の 7 つのみ。これ以外は使わず、必要なら先にユーザーへ確認する
  `arrays-hashing` / `two-pointers` / `stack` / `binary-search` /
  `sliding-window` / `linked-list` / `trees`

## 絶対に守ること: 「考えたこと / アプローチ」は本人の欄

問題の README にある `## 考えたこと / アプローチ` の**中身を Claude が書いてはいけない**。
提案・要約・清書・補完・「参考までに」の追記も含めて一切しない。ここは本人が
自分の頭で書くための欄であり、Claude が埋めると学習の記録として無意味になる。

Claude がこの節に対してしてよいのは **`### N 回目` という空の見出しを用意すること
だけ**（`new_problem.py` / `new_attempt.py` が自動で行う）。既存の記述は読んでよいが、
書き換え・削除・整形はしない。ユーザーから明示的に「ここに書いて」と頼まれた場合のみ書く。

他の節（問題の要約 / 計算量 / 学び・再利用できるパターン / 復習ログのメモ）は
Claude が書いてよい。`## 次回やること` は本人と Claude のどちらが書いてもよい節。

## 解き直し（既に同じ番号のディレクトリがある場合）

`new_problem.py` ではなく `scripts/new_attempt.py <番号>` を使う。
前回のコードが `attempts/` に退避され、README の復習ログに行が追加される。
その後 `solution.py` を今回の解答で上書きし、前回との差分を報告する。
README の考察は上書きせず追記する。詳細は `/leetcode-log` スキルを見ること。

## 問題を記録するとき（初回）

必ず `/leetcode-log` スキルの手順に従うこと。要点だけ再掲すると:

1. `python scripts/new_problem.py <番号> "<タイトル>" -c <category> -d <difficulty> --recall <自力>` で雛形を作る
   （手で mkdir しない。ファイル名の規約がずれる）。
   実行すると問題の README がエディタで自動的に開く。`--no-open` で抑止できるが、
   ユーザーがその場で考察を書けるよう、**通常は付けないこと**
2. `solution.py` にユーザーのコードを入れる
3. テストファイルに問題文の Example を写す。テストは `solution` フィクスチャを引数に取る
   （`def test_example_1(solution):` → `solution.Solution().xxx(...)`）。import は書かない
4. `./.venv/bin/python -m pytest problems/<category>/<dir>` で確認する
   （**任意**。落ちても記録は止めない。未完成・不正解のコードもそのまま保存する）
5. 問題ディレクトリの `README.md` を埋める
6. `python scripts/update_index.py` でルート README の一覧と PROGRESS.md / REVIEW.md を更新
   （どちらも自動生成なので手で編集しないこと）
7. `<番号>. <タイトル>` というメッセージでコミット（テストの成否は問わない）

## 英語で話した記録（mock interview / 一人での説明練習）

coding interview の練習として、英語で話した内容も問題に紐づけて残す。
`problems/<category>/<dir>/english/<日付>-<mock|solo>.md` に保存し、問題 README の
`## 英語での説明` からリンクする。手順は `/mock-log` スキルを見ること。

- **mock**（面接官役の前で解きながら話す）は解いた 1 回として数える。`new_attempt.py`
  （初回は `new_problem.py`）で復習ログに行を足してから `scripts/new_english.py <番号> mock` を使う
- **solo**（解いたコードを見ながら一人で説明を録音）は解いた回として数えない。
  復習ログには触らず `scripts/new_english.py <番号> solo` だけを使う
- 文字起こしはボイスメモアプリのものが貼られる。Claude が整形するが、直すのは**音声認識の誤りだけ**。
  文法・言い回し・つなぎの言葉は英語のレビューの材料なので直さない。元の文字起こしも残す
- 記録の `## 自分の振り返り` は本人の欄。「考えたこと / アプローチ」と同じく Claude は中身を書かない
- レビューのあと、記録の `## 説明の例` に、同じ解き方で通して話した例を Claude が書く。
  本人が録音と比べるためのもので、話す前に読む台本ではない（レビューより先に書かない）
- どの問題でも使える言い回しや説明の型（話す台本）は `talk-scripts/phrases.md` に一元管理する。
  レビューで見つかったら Claude が足す（出典として記録へのリンクを付け、重複は作らない）。
  ルートの `scripts/` はコード用なので混ぜない

## NeetCode 150

ユーザーは NeetCode 150 に沿って進めている。リストは `data/neetcode150.tsv`、
進捗は `PROGRESS.md`（`problems/` から自動生成）。
「次に何を解けばいい?」と聞かれたら PROGRESS.md の未着手 (⬜) から、
学習対象セクション（`problems/` にカテゴリがあるもの）を優先して提案する。
あわせて REVIEW.md の「今週やる」から解き直しも提案する（新規と復習の両方を出す）。

## 解き直しの予定（REVIEW.md）

`REVIEW.md` は忘却曲線に基づく解き直しの予定表で、`scripts/update_review.py` が
各問題 README の復習ログ（日付と「自力」列）と `## 次回やること` から生成する。
自力の記号は ◎ 何も見ずにすんなり / ○ 何も見ずに解けたが時間がかかった /
△ ヒント・解説・過去の解答を見た / × 解けなかった / ? 記録なし。
間隔は 3 → 7 → 14 → 30 → 60 日で、◎ で 1 段上がり、△ と × で 3 日に戻る（詳細は `scripts/_review.py`）。
記録するときは自力を必ず確認する。「結果」が AC でも、答えを見ながらなら △。

解き直しの予定を Google カレンダーに入れるよう頼まれたら `/review-calendar` スキルに従う。
予定の形式（7:00–9:00、通知は前日 23:00 と当日 7:00）は `scripts/review_events.py` が決めている。
カレンダーはメイン (primary) だけを使う（`.claude/hooks/calendar-guard.sh` が強制）。

## テストについて

`problems/` 配下には同名の `solution.py` が多数あるため、ルートの `conftest.py` が
パス指定で読み込む `solution` フィクスチャを提供している。テストファイル名は
問題ごとにユニークにする（`test_0242_valid_anagram.py` の形式。`new_problem.py` が自動で付ける）。
