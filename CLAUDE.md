# leet-code-logs

LeetCode で解いた問題のコードと考えを記録するリポジトリ。

## 前提

- Python。仮想環境は `.venv`（`./.venv/bin/python -m pytest` で実行する）
- 問題は `problems/<category>/<4桁番号>-<スラッグ>/` に 1 問 1 ディレクトリ
- `solution.py` は常に最新の解答。過去の解答は `attempts/<日付>.py` に残す
- 同じ問題を何度も解き直して記録するのが前提。**過去の解答とメモを消さないこと**
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
Claude が書いてよい。

## 解き直し（既に同じ番号のディレクトリがある場合）

`new_problem.py` ではなく `scripts/new_attempt.py <番号>` を使う。
前回のコードが `attempts/` に退避され、README の復習ログに行が追加される。
その後 `solution.py` を今回の解答で上書きし、前回との差分を報告する。
README の考察は上書きせず追記する。詳細は `/leetcode-log` スキルを見ること。

## 問題を記録するとき（初回）

必ず `/leetcode-log` スキルの手順に従うこと。要点だけ再掲すると:

1. `python scripts/new_problem.py <番号> "<タイトル>" -c <category> -d <difficulty>` で雛形を作る
   （手で mkdir しない。ファイル名の規約がずれる）。
   実行すると問題の README がエディタで自動的に開く。`--no-open` で抑止できるが、
   ユーザーがその場で考察を書けるよう、**通常は付けないこと**
2. `solution.py` にユーザーのコードを入れる
3. テストファイルに問題文の Example を写す。テストは `solution` フィクスチャを引数に取る
   （`def test_example_1(solution):` → `solution.Solution().xxx(...)`）。import は書かない
4. `./.venv/bin/python -m pytest problems/<category>/<dir>` で確認する
   （**任意**。落ちても記録は止めない。未完成・不正解のコードもそのまま保存する）
5. 問題ディレクトリの `README.md` を埋める
6. `python scripts/update_index.py` でルート README の一覧と PROGRESS.md を更新
   （PROGRESS.md は NeetCode 150 の進捗。自動生成なので手で編集しないこと）
7. `<番号>. <タイトル>` というメッセージでコミット（テストの成否は問わない）

## NeetCode 150

ユーザーは NeetCode 150 に沿って進めている。リストは `data/neetcode150.tsv`、
進捗は `PROGRESS.md`（`problems/` から自動生成）。
「次に何を解けばいい?」と聞かれたら PROGRESS.md の未着手 (⬜) から、
学習対象セクション（`problems/` にカテゴリがあるもの）を優先して提案する。

## テストについて

`problems/` 配下には同名の `solution.py` が多数あるため、ルートの `conftest.py` が
パス指定で読み込む `solution` フィクスチャを提供している。テストファイル名は
問題ごとにユニークにする（`test_0242_valid_anagram.py` の形式。`new_problem.py` が自動で付ける）。
