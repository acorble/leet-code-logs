# 102. Binary Tree Level Order Traversal

- URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
- 難易度: medium
- カテゴリ: trees
- 初回: 2026-08-30

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-08-30 | AC | 38分 | [solution.py](solution.py) | |

<!-- ATTEMPTS:END -->

## 問題の要約

二分木を上の階層から順に走査し、階層ごとに値をまとめたリストのリストを返す。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

- 時間: O(n^2)（`stack.pop(0)` が O(n) のため。deque を使えば O(n)）
- 空間: O(n)

## 学び・再利用できるパターン

- **レベルごとに区切る BFS**: ループの先頭で `len(queue)` を控えておき、その回数だけ
  取り出す。これで「今の階層のノードだけ」を処理できる。
  階層を意識する木の問題（199. Right Side View, 103. Zigzag Level Order など）は
  すべてこの形に乗る
- 先頭から取り出すなら `list.pop(0)` ではなく `collections.deque` の `popleft()`。
  list の pop(0) は残り全体をずらすので O(n) かかる
