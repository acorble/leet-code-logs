# 981. Time Based Key-Value Store

- URL: https://leetcode.com/problems/time-based-key-value-store/
- 難易度: medium
- カテゴリ: binary-search
- 初回: 2026-06-30

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-06-30 | AC | - | [solution.py](solution.py) | Beats 5.03%。set のたびに履歴を sort している |

<!-- ATTEMPTS:END -->

## 問題の要約

`set(key, value, timestamp)` で値を記録し、
`get(key, timestamp)` で**その時刻以下で最も新しい**値を返すデータ構造を作る。
該当が無ければ空文字を返す。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

- `set`: **O(n log n)** — 追加のたびに履歴全体を `sort()` している
- `get`: O(log n) — 二分探索
- 空間: O(n)

`set` が n 回なら全体で O(n^2 log n) になる。**Beats 5.03% の原因はここ**。

## 学び・再利用できるパターン

- **「その値以下で最大のもの」を探す二分探索**。一致したら即返し、
  一致しなくても `timeHistory[m] < timestamp` の間は候補として控えておく。
  ループを抜けたとき `targetTime` に最後に控えた値（= 条件を満たす最大）が残る
- [153](../0153-find-minimum-in-rotated-sorted-array) の
  「候補を控えながら詰める」と同じ型。ただし向きが逆（あちらは最小、こちらは最大）
- 設計問題（design）では、**どの操作が何回呼ばれるか**を意識する。
  `get` を速くしても `set` が遅ければ意味がない

### set のたびに sort しているのが致命傷（実測）

```python
self.timeHistoryMap[key].append(timestamp)
self.timeHistoryMap[key].sort()          # ← 毎回ソート
```

| set の回数 | sort あり | sort なし | 差 |
| --- | --- | --- | --- |
| 1,000 | 1.7ms | 0.2ms | 10 倍 |
| 5,000 | 31.4ms | 0.6ms | 55 倍 |
| 20,000 | 366.4ms | 1.9ms | 192 倍 |
| 100,000 | 9,036.8ms | 9.9ms | **916 倍** |

**この問題の制約は set と get 合わせて 2×10^5 回**。その規模だと桁違いに効く。

- **`sort()` は不要**。問題文が「set は timestamp が**厳密に増加する順**で呼ばれる」
  と保証しているので、`append` するだけで常に昇順が保たれる
- 保証が無い場合でも、全体を毎回ソートするのではなく
  **挿入位置を二分探索して差し込む**（`bisect.insort`）ほうが速い

→ 2 回目は「この `sort()` は本当に必要か」から考える。

### 2 つの dict は 1 つにできる

`keyMap`（key → {timestamp: value}）と `timeHistoryMap`（key → [timestamp]）の
2 本立てになっているが、**key → [(timestamp, value)] の 1 本**で足りる。
二分探索で位置を見つけたら、その場でペアの value を取り出せる。

- 同じ情報を 2 箇所に持つと、片方だけ更新して壊れる危険がある
- [110](../../trees/0110-balanced-binary-tree) の「返り値の bool が使われていない」と同じで、
  **設計が途中で 2 通り混ざった状態**

### 細かい点

`timeHistory = self.timeHistoryMap.get(key, -1)` と `-1` を番兵にしているが、
`if key not in self.timeHistoryMap: return ""` のほうが意図が素直。
リストと数値を同じ変数に入れると型が揺れる。
