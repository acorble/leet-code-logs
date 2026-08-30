# leet-code-logs

LeetCode で解いた問題のコードと考えを記録するリポジトリ。

## 前提

- Python。仮想環境は `.venv`（`./.venv/bin/python -m pytest` で実行する）
- 問題は `problems/<category>/<4桁番号>-<スラッグ>/` に 1 問 1 ディレクトリ
- カテゴリは以下の 7 つのみ。これ以外は使わず、必要なら先にユーザーへ確認する
  `arrays-hashing` / `two-pointers` / `stack` / `binary-search` /
  `sliding-window` / `linked-list` / `trees`

## 問題を記録するとき

必ず `/leetcode-log` スキルの手順に従うこと。要点だけ再掲すると:

1. `python scripts/new_problem.py <番号> "<タイトル>" -c <category> -d <difficulty>` で雛形を作る
   （手で mkdir しない。ファイル名の規約がずれる）
2. `solution.py` にユーザーのコードを入れる
3. テストファイルに問題文の Example を写す。テストは `solution` フィクスチャを引数に取る
   （`def test_example_1(solution):` → `solution.Solution().xxx(...)`）。import は書かない
4. `./.venv/bin/python -m pytest problems/<category>/<dir>` で確認する
   （**任意**。落ちても記録は止めない。未完成・不正解のコードもそのまま保存する）
5. 問題ディレクトリの `README.md` を埋める
6. `python scripts/update_index.py` でルート README の一覧を更新
7. `<番号>. <タイトル>` というメッセージでコミット（テストの成否は問わない）

## テストについて

`problems/` 配下には同名の `solution.py` が多数あるため、ルートの `conftest.py` が
パス指定で読み込む `solution` フィクスチャを提供している。テストファイル名は
問題ごとにユニークにする（`test_0242_valid_anagram.py` の形式。`new_problem.py` が自動で付ける）。
