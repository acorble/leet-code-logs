# 238. Product of Array Except Self

- URL: https://leetcode.com/problems/product-of-array-except-self/
- 難易度: medium
- カテゴリ: arrays-hashing
- 初回: 2026-06-03

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 自力 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-06-03 | - | ? | - | [attempts/2026-06-03.java](attempts/2026-06-03.java) | Java。左側の積（prefix）と右側の積（suffix）の配列を作って掛け合わせる |

<!-- ATTEMPTS:END -->

## 次回やること

<!-- 次に解き直すときに試したいこと。`- [ ] ...` の形で書き、済んだら行ごと消す。本人も Claude も書いてよい -->

- [ ] Python で解く
- [ ] follow-up: `prefixes` / `suffixes` の配列を使わず、答えの配列だけで解く（追加の空間 O(1)）

## 問題の要約

整数の配列 `nums` について、`answer[i]` = **`nums[i]` 以外のすべての要素の積** となる配列を返す。
**割り算を使わずに** O(n) で解くこと。follow-up は「答えの配列以外の追加の空間を O(1) にできるか」。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

- 時間: **O(n)** — 左から 1 周（prefix）、右から 1 周（suffix と答え）
- 空間: **O(n)** — 答えとは別に `prefixes` と `suffixes` の 2 本（follow-up の O(1) にはなっていない）

## 学び・再利用できるパターン

### 「自分以外」は「自分の左側」×「自分の右側」

`nums[i]` 以外の積は、**i より左の積**と **i より右の積**を掛けたものになる。

```
nums      =  1   2   3   4
prefixes  =  1   1   2   6     ← i より左の積（左端は何もないので 1）
suffixes  = 24  12   4   1     ← i より右の積（右端は何もないので 1）
answer    = 24  12   8   6     ← prefixes[i] × suffixes[i]
```

「全体の積 ÷ `nums[i]`」なら一瞬だが、0 が含まれると割れない（そもそも割り算は禁止）。
左右に分けて、それぞれを**1 つ前の結果に 1 回掛けるだけ**で積み上げていくのがこの方法。
「左からの累積」と「右からの累積」を組み合わせる形は、配列の問題で何度も出てくる
（足し算なら累積和。[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) も左右それぞれの最大値を使う）。

### follow-up: 配列 2 本を使わずに O(1) にする

`prefixes` は答えの配列 `answer` にそのまま書いておき、`suffix` は**変数 1 つ**で持ちながら右から掛けていけばよい。

```python
answer = [1] * n
for i in range(1, n):            # 左から: answer[i] = i より左の積
    answer[i] = answer[i - 1] * nums[i - 1]
suffix = 1
for i in range(n - 1, -1, -1):   # 右から: 右側の積を掛け足していく
    answer[i] *= suffix
    suffix *= nums[i]
```

今回の解答も、2 周目では `suffixes[i+1]` しか使っていないので、`suffixes` を配列で持たなくてよい。
答えの配列は「出力」なので、追加の空間には数えない決まりになっている。

### 細かい点（Java）

- 2 周目のループは `i = nums.length - 2` から始まるので、最後の要素の答えだけをループの後で
  `answer[nums.length - 1] = prefixes[nums.length - 1]` と別に入れている。
  ループを `nums.length - 1` から始めて `suffixes[i+1]` の読み出しを工夫すれば、特別扱いは要らなくなる（上の Python 版がその形）
- 1 周目のコメント「store the product of the prefix and the suffix in answer[i]」は、実際には `prefixes[i]` に入れている。
  コピーしたときの名残
