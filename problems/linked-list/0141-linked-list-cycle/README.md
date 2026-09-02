# 141. Linked List Cycle

- URL: https://leetcode.com/problems/linked-list-cycle/
- 難易度: easy
- カテゴリ: linked-list
- 初回: 2026-07-05

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-07-05 | - | - | [attempts/2026-07-05.py](attempts/2026-07-05.py) | |
| 2 | 2026-07-10 | - | - | [solution.py](solution.py) | set をやめて Floyd の slow/fast に。O(1) 空間 |

<!-- ATTEMPTS:END -->

## 問題の要約

連結リストが循環しているか（どこかのノードの `next` が前のノードに戻っているか）を判定する。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

### 2 回目
一応通ったが、ループ条件が非標準で自分でも正しさを疑った。
標準形は while fast and fast.next。


## 計算量

| 回 | 手段 | 時間 | 空間 |
| --- | --- | --- | --- |
| 1 | 見たノードを set に溜める | O(n) | **O(n)** |
| 2 | Floyd の slow / fast | O(n) | **O(1)** |

## 学び・再利用できるパターン

- **「既に見たか」を set で持つ**のは、循環検出のいちばん素直な形。
  [217. Contains Duplicate](../../arrays-hashing/0217-contains-duplicate)
  と同じ発想で、対象が数値からノードに変わっただけ
- **set に入れるのはノードそのもの（値ではない）**。値で判定すると、
  同じ値のノードが並んでいるだけで循環と誤判定する
  （テストの `test_duplicate_values_no_cycle` がそのケース）。
  Python のオブジェクトは既定で「同一性」でハッシュされるので、そのまま set に入れてよい

### O(1) 空間の定石: Floyd の循環検出（2 回目で到達）

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

### 2 回目で変わったこと

- set をやめ、ポインタ 2 本だけに → 空間 **O(n) → O(1)**
- `slow, fast = head, head.next` と**半歩ずらして**始めている。
  同じ位置から始めると最初の比較で必ず一致してしまうため、
  ずらすか「進めてから比較する」かのどちらかが要る。ここは前者
- 停止条件が `while fast.next and fast.next.next:` になっている。
  循環があれば `next` が尽きないのでループは抜けず、
  無ければ fast が先に末尾に達して抜ける

### 翌日への繋がり（時系列）

- **7/5**: 1 回目。set で解く
- **7/10**: 2 回目。slow / fast を使えるようになる
- **7/11**: [143. Reorder List](../0143-reorder-list) の 2 回目で、
  同じ slow / fast を**中点探索**に使って O(1) 空間を達成

141 で手に入れた道具を、翌日に別の問題で使っている。

### 細かい点

`if slow == fast` は `is` のほうが意図に近い。
`ListNode` は `__eq__` を定義していないので `==` も同一性比較になり結果は同じだが、
「同じオブジェクトか」を見たいなら `is` と書くほうが誤解がない。
