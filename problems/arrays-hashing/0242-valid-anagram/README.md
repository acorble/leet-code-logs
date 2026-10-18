# 242. Valid Anagram

- URL: https://leetcode.com/problems/valid-anagram/
- 難易度: easy
- カテゴリ: arrays-hashing
- 初回: 2026-04-12

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 自力 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-04-12 | - | ? | - | [attempts/2026-04-12.java](attempts/2026-04-12.java) | Java。両方を 1 文字ずつに分けてソートし、つなぎ直して比較 |
| 2 | 2026-04-18 | - | ? | - | [attempts/2026-04-18.java](attempts/2026-04-18.java) | Java。HashMap で文字ごとの個数を数え、2 つの Map を比較 |

<!-- ATTEMPTS:END -->

## 次回やること

<!-- 次に解き直すときに試したいこと。`- [ ] ...` の形で書き、済んだら行ごと消す。本人も Claude も書いてよい -->

- [ ] Python で解く（まず `dict` で数える。そのあと `collections.Counter` でも書いてみる）
- [ ] 最初に長さを比べて、違えばすぐ `False` を返す

## 問題の要約

2 つの文字列 `s` と `t` が**アナグラム**（同じ文字を同じ個数ずつ使って並べ替えたもの）かどうかを判定する。
文字は英小文字だけ。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

### 2 回目

## 計算量

n は文字列の長さ。

| | 1 回目（ソート） | 2 回目（HashMap で数える） |
| --- | --- | --- |
| 時間 | **O(n log n)** — ソートが支配的 | **O(n)** — 1 文字ずつ数えるだけ |
| 空間 | O(n) — 1 文字ずつの配列と、つなぎ直した文字列 | O(1) — キーは英小文字の最大 26 種類（`split("")` の配列は O(n)） |

## 学び・再利用できるパターン

### 「並べ替えて同じか」は「個数が同じか」に言い換えられる

アナグラムかどうかは、**並び順を無視して、どの文字が何個あるか**だけで決まる。

- 1 回目のソートは、並び順を消すための方法。並べ替えれば、アナグラム同士は同じ文字列になる
- 2 回目の HashMap は、最初から並び順を見ずに個数だけを数える方法。ソートの O(n log n) が要らなくなる

1 回目 → 2 回目で、「並べ替えて比べる」から「数えて比べる」に変わっていて、計算量が O(n log n) から O(n) に改善している。
「個数を数えて比べる」は、[567. Permutation in String](../../sliding-window/0567-permutation-in-string) と同じ考え方
（567 は、それを幅を固定した窓の中で行う）。

### 数える Map は 1 つで足りる

2 回目は Map を 2 つ作って最後に比べている。1 つの Map で、`s` の文字は +1、`t` の文字は -1 すれば、
アナグラムなら最後に全部 0 になる。

```python
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    count = {}
    for a, b in zip(s, t):
        count[a] = count.get(a, 0) + 1
        count[b] = count.get(b, 0) - 1
    return all(v == 0 for v in count.values())
```

文字が英小文字だけと分かっているなら、Map の代わりに長さ 26 の配列でもよい
（`ord(c) - ord('a')` を添え字にする）。Python なら `Counter(s) == Counter(t)` の 1 行でも書ける。

### 細かい点（Java）

- `if (x.equals(y)) { return true; } return false;` は `return x.equals(y);` と同じ
- 2 回目の「無ければ 1、あれば +1」は `maps.put(c, maps.getOrDefault(c, 0) + 1);` か
  `maps.merge(c, 1, Integer::sum);` の 1 行で書ける
- 長さが違えば必ずアナグラムではないので、最初に `s.length() != t.length()` を確かめると、無駄な処理を省ける
