# 875. Koko Eating Bananas

- URL: https://leetcode.com/problems/koko-eating-bananas/
- 難易度: medium
- カテゴリ: binary-search
- 初回: 2026-06-27

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-06-27 | AC | - | [solution.py](solution.py) | 答えの範囲を二分探索する |

<!-- ATTEMPTS:END -->

## 問題の要約

バナナの山があり、1 時間に k 本まで食べられる（山をまたいで食べることはできない）。
h 時間以内に全部食べ切れる**最小の k** を返す。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

- 時間: O(n × log(max(piles))) — 速度の候補を二分探索し、各候補で全山を走査する
- 空間: O(1) — `range` は遅延オブジェクトなので実際に配列を作らない

## 学び・再利用できるパターン

- **答えそのものを二分探索する**（binary search on the answer）。
  [704](../0704-binary-search) や [74](../0074-search-a-2d-matrix) は
  「配列の中から探す」だったが、この問題は探す対象が**配列に存在しない**。
  速度 k は 1 〜 max(piles) のどこかにある、という**値の範囲**を二分探索する
- 成立する条件が **単調**なのが鍵。k が間に合うなら k+1 も必ず間に合う。
  この単調性があるとき、「間に合う最小の k」を二分探索で見つけられる
- **判定を別関数に切り出す**（`ifFinishEating`）と見通しがよい。
  「探す」と「判定する」を分ける形は
  [572. Subtree](../../trees/0572-subtree-of-another-tree) と同じ構造
- `while left < right` + `right = m` / `left = m + 1` は
  **「条件を満たす最小のものを探す」ときの型**。
  条件を満たしたら m を答えの候補として残す（`right = m`）ので、
  704 や 74 の「見つけたら即 return」とは形が違う

### 上限を max(piles) にできる理由

1 時間に max(piles) 本食べられれば、どの山も 1 時間で終わる。
つまり全部で len(piles) 時間。制約が `len(piles) <= h` なので必ず間に合う。
→ 答えは必ず 1 〜 max(piles) の範囲にあり、探索範囲をこれ以上広げる必要はない。

### 細かい点

- `numberOfBananas = range(1, max(piles) + 1)` は `range` なので、
  10 億要素でもメモリを食わない（遅延評価）。ただし添字と値が 1 ずれるため、
  `numberOfBananas[m]` の変換が要る。
  **`left, right = 1, max(piles)` と値そのものを範囲にすれば、この変換は不要**
- 切り上げの割り算は 3 通り書ける。どれでも同じ

  ```python
  if pile % k == 0: h += pile // k        # 今の書き方
  else:             h += pile // k + 1
  h += math.ceil(pile / k)                 # float 経由（巨大値だと誤差の恐れ）
  h += -(-pile // k)                       # 整数のみ。イディオム
  ```
