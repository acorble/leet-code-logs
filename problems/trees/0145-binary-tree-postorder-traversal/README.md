# 145. Binary Tree Postorder Traversal

- URL: https://leetcode.com/problems/binary-tree-postorder-traversal/
- 難易度: easy
- カテゴリ: trees
- 初回: 2026-10-10

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-10-10 | - | - | [solution.py](solution.py) | 再帰 DFS。NeetCode 150 外 |

<!-- ATTEMPTS:END -->

## 問題の要約

二分木を **後順（postorder: 左 → 右 → 自分）** で辿り、ノードの値を訪問順に並べて返す。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

- 時間: **O(n)** — 各ノードを 1 回ずつ訪問する
- 空間: **O(h)** の再帰スタック（h は木の高さ。偏った木なら O(n)）＋ 出力の O(n)

## 学び・再利用できるパターン

### 3 つの走査順は「append をどこに置くか」だけの違い

```python
def dfs(node):
    if not node:
        return
    # ← ここで append すると前順 (preorder):  自分 → 左 → 右
    dfs(node.left)
    # ← ここで append すると中順 (inorder):   左 → 自分 → 右
    dfs(node.right)
    # ← ここで append すると後順 (postorder): 左 → 右 → 自分
```

- **前順**: 親を先に処理したいとき（木のコピー、シリアライズ）
- **中順**: BST なら値が小さい順に出る
  （[230](../0230-kth-smallest-element-in-a-bst)、[98](../0098-validate-binary-search-tree)）
- **後順**: 子の結果を集めてから親を決めたいとき。
  [104](../0104-maximum-depth-of-binary-tree)、[110](../0110-balanced-binary-tree)、
  [543](../0543-diameter-of-binary-tree) の「左右の戻り値を見て自分の値を返す」DFS は、
  どれも後順の形をしている

### 再帰を使わない書き方（follow-up）

LeetCode の follow-up は「iterative で解けるか」。後順はスタックで書くのが 3 つの中で一番面倒だが、
**「自分 → 右 → 左」の前順で集めて最後に反転する**と簡単に書ける。

```python
stack, ret = [root] if root else [], []
while stack:
    node = stack.pop()
    ret.append(node.val)
    if node.left:
        stack.append(node.left)
    if node.right:
        stack.append(node.right)
return ret[::-1]
```

### 細かい点

- `nonlocal ret` は不要。`append` はリストの中身を変えるだけで、名前を付け替えないため
  （[230 の学び](../0230-kth-smallest-element-in-a-bst) と同じ話）
- `dfs` 末尾の `return` は無くても同じ
