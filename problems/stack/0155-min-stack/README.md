# 155. Min Stack

- URL: https://leetcode.com/problems/min-stack/
- 難易度: medium
- カテゴリ: stack
- 初回: 2026-06-21

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 自力 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-06-21 | - | ? | - | [solution.py](solution.py) | 値の Stack と「その時点の最小値」の Stack を並べて持つ。10/18 に後から記録 |

<!-- ATTEMPTS:END -->

## 次回やること

<!-- 次に解き直すときに試したいこと。`- [ ] ...` の形で書き、済んだら行ごと消す。本人も Claude も書いてよい -->

- [ ] Stack を 1 本にして、`(値, その時点の最小値)` の組を積む形で書く

## 問題の要約

`push` / `pop` / `top` に加えて、**今入っている値の最小値**を返す `getMin` を持つ Stack を作る。
どの操作も O(1) で行うこと。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

- 時間: **O(1)** — 4 つの操作すべて。`getMin` も `minArr[-1]` を読むだけ
- 空間: **O(n)** — 値と同じ数だけ `minArr` にも積むので、Stack 2 本分

## 学び・再利用できるパターン

### 「その時点の答え」を値と一緒に積んでおく

`getMin` を O(1) にするために、`push` のたびに**その時点の最小値**を `minArr` に積んでいる。

```
push:     -2     0    -3
stack:  [-2]  [-2,0]  [-2,0,-3]
minArr: [-2]  [-2,-2] [-2,-2,-3]   ← minArr[i] = stack[0..i] の最小値
```

`pop` で `stack` と `minArr` を同時に 1 つ減らせば、`minArr[-1]` は**残っている値の最小値**に自動で戻る。
最小値を探し直す必要がないのがこの方法の要点。

単純に「最小値を 1 つの変数で持つ」だけだと、最小値を `pop` したときに次の最小値が分からず、
全体を探し直して O(n) になる（`test_min_restored_after_pop` はこれを確かめている）。

### 同じ考え方の別の書き方

**Stack を 1 本にして組を積む**（次回やること）

```python
def push(self, val):
    cur_min = min(val, self.stack[-1][1]) if self.stack else val
    self.stack.append((val, cur_min))
```

2 本の Stack の長さが必ずそろうので、片方だけ push / pop し忘れるバグが起きない。

**最小値が更新されたときだけ積む**（空間の節約）

`minArr` には、`val <= minArr[-1]` のときだけ積み、`pop` した値が `minArr[-1]` と等しいときだけ `minArr` も pop する。
同じ最小値が 2 回積まれる場合に備えて、`<` ではなく **`<=`** にするのがポイント
（`test_duplicate_minimum` のケース。`<` だと 1 回目の pop で最小値の記録が消える）。

### 細かい点

- `push` の `if self.minArr: ... else: ...` は、`min(self.minArr[-1], value) if self.minArr else value` と 1 行にもできる
