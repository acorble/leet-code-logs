# leet-code-logs

LeetCode で解いた問題のコードと、解いたときの考えを記録するリポジトリ。

- 言語: Python
- 分類: アルゴリズムのカテゴリ別 (`problems/<category>/<番号>-<スラッグ>/`)
- 進め方: [NeetCode 150](https://neetcode.io/practice) に沿って進める → **[進捗はこちら](PROGRESS.md)**

## ディレクトリ構成

```
problems/
  arrays-hashing/
    0001-two-sum/
      README.md              # 問題メモ + 復習ログ
      solution.py            # 最新の解答
      attempts/              # 過去の解答 (2026-08-30.py ...)
      test_0001_two_sum.py   # サンプルケースのテスト
  two-pointers/
  ...
PROGRESS.md         # NeetCode 150 の進捗 (自動生成。手で編集しない)
data/
  neetcode150.tsv   # NeetCode 150 の問題リスト
scripts/
  new_problem.py    # 問題ディレクトリの雛形を作る
  new_attempt.py    # 解き直し。前回のコードを attempts/ に退避する
  _open_editor.py   # 作成後に README をエディタで開く
  update_index.py   # 下の一覧テーブルと PROGRESS.md を再生成する
  update_progress.py # PROGRESS.md だけを再生成する
templates/          # 雛形の元ファイル
conftest.py         # solution.py を読み込む pytest フィクスチャ
CLAUDE.md           # Claude 向けのリポジトリ規約
.claude/skills/leetcode-log/   # 「解いた問題を記録する」手順
```

## セットアップ

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## 使い方

### Claude に任せる場合（普段はこちら）

Claude Code でこのリポジトリを開き、解いたコードを貼って
「242 Valid Anagram 解いた」のように伝えるだけでよい。
解き直したときも同じ。前回のコードは自動で `attempts/` に残り、前回との差分が報告される。
`/leetcode-log` スキルが、雛形作成・テスト作成と実行・メモの下書き・
一覧更新・コミットまでを行う。メモは後から自分の言葉に直せばよい。

以下は手動でやる場合の手順。

### 1. 新しい問題を始める

```bash
python scripts/new_problem.py 1 "Two Sum" --category arrays-hashing --difficulty easy
```

`problems/arrays-hashing/0001-two-sum/` に README・solution.py・テストが作られ、
**その問題の README がエディタで自動的に開く**（開きたくないときは `--no-open`）。
カテゴリを増やしたいときは `mkdir problems/<category>` してから指定する。

### 2. 解いてテストする（任意）

```bash
pytest                                  # 全部
pytest problems/arrays-hashing/0001-two-sum   # 1 問だけ
```

テストは正解を保証するためではなく、後で解き直したときに壊れていないか気づくためのもの。
未完成のコードや通らないコードもそのまま記録してよい。

テストは `solution` フィクスチャで同じディレクトリの `solution.py` を受け取る。

```python
def test_example_1(solution):
    assert solution.Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
```

### 3. 同じ問題を解き直す

```bash
python scripts/new_attempt.py 1 --result AC --minutes 6分 --note "今回はヒント無し"
```

前回の `solution.py` が `attempts/<日付>.py` にコピーされ、問題の README の
復習ログに新しい行が追加され、**README がエディタで開く**。
あとは `solution.py` を今回の解答で上書きする。

退避先のファイル名は「そのコードを書いた日」。同じ日に複数回解いた場合は
`2026-07-11.py`, `2026-07-11-2.py` と連番になる。
過去の日付で記録したいときは `--date 2026-07-11` を付ける。

`solution.py` は常に最新、`attempts/` に過去が積み上がる。前回との比較は:

```bash
diff problems/arrays-hashing/0001-two-sum/attempts/2026-08-30.py \
     problems/arrays-hashing/0001-two-sum/solution.py
```

解き直すたびに、README の「考えたこと / アプローチ」に `### N 回目` の空見出しが
自動で追加される。**この節は自分の手で書く欄で、Claude は中身を書かない。**
同じ問題を 3 回、5 回と解いたときの記述の差が、そのまま上達の記録になる。

### 4. 一覧と進捗を更新する

```bash
python scripts/update_index.py
```

この README の一覧と [PROGRESS.md](PROGRESS.md) の両方が更新される。
進捗のチェックは手で付けない。`problems/` に問題ディレクトリがあれば
自動で ✅ になる仕組みなので、記録とチェックがズレることがない。

## カテゴリ

| ディレクトリ | 分類 |
| --- | --- |
| `arrays-hashing` | Arrays & Hashing |
| `two-pointers` | Two Pointers |
| `stack` | Stack |
| `binary-search` | Binary Search |
| `sliding-window` | Sliding Window |
| `linked-list` | Linked List |
| `trees` | Trees |

学習範囲を広げたくなったら `mkdir problems/<category>` でディレクトリを足すだけでよい
（スクリプト側の変更は不要）。

## 解いた問題一覧

<!-- INDEX:START -->

合計 21 問 / のべ 31 回

| # | 問題 | 難易度 | カテゴリ | 回数 | 最後に解いた日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [1. Two Sum](problems/arrays-hashing/0001-two-sum) | easy | arrays-hashing | 2 | 2026-07-11 |
| 217 | [217. Contains Duplicate](problems/arrays-hashing/0217-contains-duplicate) | easy | arrays-hashing | 1 | 2026-08-16 |
| 74 | [74. Search a 2D Matrix](problems/binary-search/0074-search-a-2d-matrix) | medium | binary-search | 1 | 2026-06-26 |
| 153 | [153. Find Minimum in Rotated Sorted Array](problems/binary-search/0153-find-minimum-in-rotated-sorted-array) | medium | binary-search | 1 | 2026-06-28 |
| 704 | [704. Binary Search](problems/binary-search/0704-binary-search) | easy | binary-search | 2 | 2026-06-24 |
| 875 | [875. Koko Eating Bananas](problems/binary-search/0875-koko-eating-bananas) | medium | binary-search | 1 | 2026-06-27 |
| 981 | [981. Time Based Key-Value Store](problems/binary-search/0981-time-based-key-value-store) | medium | binary-search | 1 | 2026-06-30 |
| 21 | [21. Merge Two Sorted Lists](problems/linked-list/0021-merge-two-sorted-lists) | easy | linked-list | 1 | 2026-07-04 |
| 141 | [141. Linked List Cycle](problems/linked-list/0141-linked-list-cycle) | easy | linked-list | 2 | 2026-07-10 |
| 143 | [143. Reorder List](problems/linked-list/0143-reorder-list) | medium | linked-list | 2 | 2026-07-11 |
| 206 | [206. Reverse Linked List](problems/linked-list/0206-reverse-linked-list) | easy | linked-list | 4 | 2026-07-04 |
| 100 | [100. Same Tree](problems/trees/0100-same-tree) | easy | trees | 1 | 2026-08-26 |
| 102 | [102. Binary Tree Level Order Traversal](problems/trees/0102-binary-tree-level-order-traversal) | medium | trees | 2 | 2026-08-30 |
| 104 | [104. Maximum Depth of Binary Tree](problems/trees/0104-maximum-depth-of-binary-tree) | easy | trees | 1 | 2026-07-23 |
| 110 | [110. Balanced Binary Tree](problems/trees/0110-balanced-binary-tree) | easy | trees | 1 | 2026-08-22 |
| 199 | [199. Binary Tree Right Side View](problems/trees/0199-binary-tree-right-side-view) | medium | trees | 1 | 2026-09-02 |
| 226 | [226. Invert Binary Tree](problems/trees/0226-invert-binary-tree) | easy | trees | 3 | 2026-08-19 |
| 235 | [235. Lowest Common Ancestor of a Binary Search Tree](problems/trees/0235-lowest-common-ancestor-of-a-binary-search-tree) | medium | trees | 1 | 2026-08-29 |
| 543 | [543. Diameter of Binary Tree](problems/trees/0543-diameter-of-binary-tree) | easy | trees | 1 | 2026-07-28 |
| 572 | [572. Subtree of Another Tree](problems/trees/0572-subtree-of-another-tree) | easy | trees | 1 | 2026-08-28 |
| 1448 | [1448. Count Good Nodes in Binary Tree](problems/trees/1448-count-good-nodes-in-binary-tree) | medium | trees | 1 | 2026-09-03 |

<!-- INDEX:END -->
