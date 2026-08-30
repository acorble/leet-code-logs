# leet-code-logs

LeetCode で解いた問題のコードと、解いたときの考えを記録するリポジトリ。

- 言語: Python
- 分類: アルゴリズムのカテゴリ別 (`problems/<category>/<番号>-<スラッグ>/`)

## ディレクトリ構成

```
problems/
  arrays-hashing/
    0001-two-sum/
      README.md              # 問題メモ (アプローチ・計算量・学び)
      solution.py            # 提出したコード
      test_0001_two_sum.py   # サンプルケースのテスト
  two-pointers/
  ...
scripts/
  new_problem.py    # 問題ディレクトリの雛形を作る
  update_index.py   # 下の一覧テーブルを再生成する
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
`/leetcode-log` スキルが、雛形作成・テスト作成と実行・メモの下書き・
一覧更新・コミットまでを行う。メモは後から自分の言葉に直せばよい。

以下は手動でやる場合の手順。

### 1. 新しい問題を始める

```bash
python scripts/new_problem.py 1 "Two Sum" --category arrays-hashing --difficulty easy
```

`problems/arrays-hashing/0001-two-sum/` に README・solution.py・テストが作られる。
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

### 3. 一覧を更新する

```bash
python scripts/update_index.py
```

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

合計 1 問

| # | 問題 | 難易度 | カテゴリ | 解いた日 |
| --- | --- | --- | --- | --- |
| 1 | [1. Two Sum](problems/arrays-hashing/0001-two-sum) | easy | arrays-hashing | 2026-08-30 |

<!-- INDEX:END -->
