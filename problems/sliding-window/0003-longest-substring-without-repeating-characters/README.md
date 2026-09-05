# 3. Longest Substring Without Repeating Characters

- URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- 難易度: medium
- カテゴリ: sliding-window
- 初回: 2026-06-16

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-06-16 | AC | - | [solution.py](solution.py) | 窓を set で持ち、重複が出たら左を詰める |

<!-- ATTEMPTS:END -->

## 問題の要約

文字が重複しない**連続した部分文字列**のうち、最も長いものの長さを返す。
部分列ではなく連続していることが条件（`pwwkew` の答えは `wke` の 3）。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

- 時間: O(n) 相当だが、重複のたびに `s[left:right]` を作るぶん定数倍が重い
  （実測で約 2 倍。スライスの長さは窓に比例するので、窓が大きいほど不利）
- 空間: O(min(n, 文字種)) — 窓の中の文字を set で持つ

## 学び・再利用できるパターン

- **本来のスライディングウィンドウ**。`right` を伸ばし、条件が壊れたら `left` を詰める。
  [121](../0121-best-time-to-buy-and-sell-stock) は左を「乗り換える」だけだったが、
  こちらは**窓を縮める**。これがこの型の基本形
- 窓の中身を **set** で持ち、`s[right] in charSet` で条件を判定する。
  `left` を進めるときは、set からも忘れず取り除く（この対応が崩れるとバグる）
- `abba` のように、**左端より前にある重複は窓の外**なので縮める必要がない。
  「文字列全体に重複があるか」ではなく「**窓の中に**あるか」を見るのが肝

### `duplicated` を求めるスライスは不要（検証済み）

```python
duplicated = s[left:right].index(s[right])   # ← この行
i = 0
while s[right] in charSet:
    charSet.remove(s[left + i])
    i += 1
left = left + duplicated + 1                  # ← left + i と常に同じ
```

while ループは「`s[right]` が消えるまで」左から取り除くので、
**取り除いた個数 `i` は `duplicated + 1` と必ず一致する**。
つまり `left = left + i` と書けば、スライスも `index` も要らない。

- 等価性: 12,000 パターンのランダム文字列で確認（不一致なし）
- 速度: 実測で **約 2 倍**の差。スライスは窓の長さぶんコピーが走るため

→ 2 回目は「同じ情報を 2 通りの方法で求めていないか」を見る。

### 記録について

同日に 2 回提出していて Beats は 19.65% → 70.81% だったが、
**コードの差はデバッグ用 print の有無だけ**だったので、
clean な版のみを残している。

print は 1 文字ごとに標準出力へ書くので、これは**実際に遅くなる**変更
（[21](../../linked-list/0021-merge-two-sorted-lists) では print を消したのに
Beats が下がったので、そちらは純粋な測定ノイズ）。
いずれにせよ**アルゴリズムは同一**で、記録として残す価値のある差ではない。
