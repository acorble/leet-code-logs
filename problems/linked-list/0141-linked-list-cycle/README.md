# 141. Linked List Cycle

- URL: https://leetcode.com/problems/linked-list-cycle/
- 難易度: easy
- カテゴリ: linked-list
- 初回: 2026-07-05

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-07-05 | - | - | [solution.py](solution.py) | |

<!-- ATTEMPTS:END -->

## 問題の要約

連結リストが循環しているか（どこかのノードの `next` が前のノードに戻っているか）を判定する。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

- 時間: O(n) — 各ノードを 1 回ずつ見る
- 空間: **O(n)** — 見たノードを set に溜める

空間 O(1) で解く定石がある（→ 学びの節）。

## 学び・再利用できるパターン

- **「既に見たか」を set で持つ**のは、循環検出のいちばん素直な形。
  [217. Contains Duplicate](../../arrays-hashing/0217-contains-duplicate)
  と同じ発想で、対象が数値からノードに変わっただけ
- **set に入れるのはノードそのもの（値ではない）**。値で判定すると、
  同じ値のノードが並んでいるだけで循環と誤判定する
  （テストの `test_duplicate_values_no_cycle` がそのケース）。
  Python のオブジェクトは既定で「同一性」でハッシュされるので、そのまま set に入れてよい

### O(1) 空間の定石: Floyd の循環検出

slow が 1 歩進む間に fast が 2 歩進む。**循環があれば必ず fast が slow に追いつく**
（輪の中で 1 周ぶんの差が毎回 1 ずつ縮まるため）。循環が無ければ fast が先に末尾に着く。

```
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:
        return True
return False
```

- set が要らないので空間 O(1)
- この slow / fast は
  [143. Reorder List](../0143-reorder-list) の 2 回目（7/11）で
  **中点を探すため**に使っているものと同じ道具。
  用途が「中点を探す」か「追いつくか見る」かで変わるだけ
