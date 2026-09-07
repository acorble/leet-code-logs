# 98. Validate Binary Search Tree

- URL: https://leetcode.com/problems/validate-binary-search-tree/
- 難易度: medium
- カテゴリ: trees
- 初回: 2026-09-07

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-09-07 | AC | - | [solution.py](solution.py) | 部分木の (BSTか, 最小, 最大) を下から持ち上げる |

<!-- ATTEMPTS:END -->

## 問題の要約

二分探索木として正しいかを判定する。条件は
**「左部分木の全ノード < 自分 < 右部分木の全ノード」**。
直前の親とだけ比べれば済む話ではなく、部分木の全体と比べる必要がある。
等しい値は許されない（狭義）。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->
DFSで解いた。
helper関数の引数でもrootを使うとややこしいからnodeとかのほうが良いかも。あと数値だと0のときもfalsyになるらしく、if not valみたいな判定だとfalsyだからtrueになってしまう。これを知らず判定がうまく通らずテストケース落ちていた。学び。
minEver = minValLeft if minValLeft is not None else root.val
を最初、
minEver = minValLeft or root.val
と書いていた。その後、
minEver = minValLeft if not minValLeft else root.val
と直したがこれもだめ。minValLeftが0のときfalsyなので引っかかってしまうため。

minValRight is None or root.val < minValRight
の条件も最初、
not minValRight or root.val < minValRight
のように書いていて、minValRightが0のときにfalsyでtrueになってしまってテストケース落ちてた（falseになるべきなのにtrueになっていた）

## 計算量

- 時間: **O(n)** — 各ノードを 1 回ずつ訪れ、そこでの判定は O(1)
- 空間: O(h) — 再帰スタック

**これが最適**。全ノードを見ないと判定できないので O(n) 未満にはできない。

## 学び・再利用できるパターン

- **部分木の状態をタプルで持ち上げる DFS**。各ノードが
  `(BST か, 部分木の最小, 部分木の最大)` を返し、親がそれを合成する。
  [110. Balanced](../0110-balanced-binary-tree)（深さと判定）や
  [235. LCA](../0235-lowest-common-ancestor-of-a-binary-search-tree)（発見フラグ）と同じ型
- 判定は **「左の最大 < 自分 < 右の最小」**。
  局所的に親子だけ見ると、深い位置の違反を見逃す
  （テストの `test_violation_deep_in_subtree` がそのケース）
- **最小は左だけ、最大は右だけ**から取れる。BST が成立している前提なら
  部分木の最小は必ず左端、最大は必ず右端にあるため、
  `min(左の最小, 自分, 右の最小)` のように全部を比べる必要がない。
  この省略に気づけているのが良い

```python
minEver = minValLeft  if minValLeft  is not None else root.val   # 左が無ければ自分が最小
maxEver = maxValRight if maxValRight is not None else root.val   # 右が無ければ自分が最大
```

### 235 との対比（BST の性質を使えたか）

- **8/29（[235. LCA](../0235-lowest-common-ancestor-of-a-binary-search-tree)）**:
  BST なのに大小関係を一度も使わず、全ノードを探索していた（Beats 26%）
- **9/7（この問題）**: BST の性質そのものを扱い、
  「左は必ず小さい・右は必ず大きい」を判定の軸にできている

同じ BST の問題で、性質を使えるようになっている。

### 別解: 上から範囲を渡す

下から (min, max) を持ち上げる代わりに、
**上から「取りうる値の範囲」を渡していく**書き方もある。

```
dfs(node, low, high):  low < node.val < high を満たすか
  左へ: dfs(node.left,  low,       node.val)
  右へ: dfs(node.right, node.val,  high)
```

- 返り値が bool 1 つで済み、タプルの分解が要らない
- 計算量は同じ O(n) / O(h)。**どちらでもよいが、返す情報が少ないぶん短くなる**
- 「下から持ち上げる」か「上から渡す」かは木の問題で繰り返し出てくる分かれ道

### 細かい点

判定の `if` が 1 行に 4 条件を詰めていて長い。
`leftOk = maxValLeft is None or maxValLeft < root.val` のように
名前を付けて分けると、条件の意味が読み取りやすくなる。

正しさは小さい木の総当たり（形 10 種 × 値の全組み合わせ）と
ランダム 500 本で、中順走査による判定と突き合わせて確認済み。
