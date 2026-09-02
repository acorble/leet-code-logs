# 21. Merge Two Sorted Lists

- URL: https://leetcode.com/problems/merge-two-sorted-lists/
- 難易度: easy
- カテゴリ: linked-list
- 初回: 2026-07-04

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-07-04 | AC | - | [solution.py](solution.py) | |

<!-- ATTEMPTS:END -->

## 問題の要約

昇順に並んだ 2 本の連結リストを、1 本の昇順リストに繋ぎ合わせて返す。
新しくノードを作らず、既存のノードを繋ぎ替える。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

- 時間: O(n + m) — 両方のノードを 1 回ずつ見る
- 空間: O(1) — ノードを新しく作らず、繋ぎ替えるだけ

## 学び・再利用できるパターン

- **2 本のリストを同時に進めて、小さいほうを繋ぐ**。マージソートの併合と同じ動き
- **`<=` にしているのが正しい**。`<` にすると同じ値のとき list2 が先に来て、
  元の順序が保たれない（安定性が崩れる）
- この処理は [143. Reorder List](../0143-reorder-list) の 2 回目で使った
  「前半と後半を交互に繋ぐ」の一般形。**7/4 の時点で既に書けていた**

### ダミーノードを使うと短くなる

今の実装は「最初の 1 個をどちらから取るか」を while の前で決めている。
先頭にダミーを 1 個置くと、この前処理が丸ごと要らなくなる。

```python
dummy = ListNode()
tail = dummy
while list1 and list2:
    if list1.val <= list2.val:
        tail.next, list1 = list1, list1.next
    else:
        tail.next, list2 = list2, list2.next
    tail = tail.next
tail.next = list1 or list2      # 残りをまとめて繋ぐ
return dummy.next
```

- **`tail.next = list1 or list2`** で、余ったほうを 1 行で繋げる。
  今の実装は残りを 1 個ずつループで繋いでいるが、既に繋がっているので
  まとめて 1 回で済む
- ダミーノードは「先頭が決まるまで返り値を保持できない」問題を消すための定石。
  連結リストの問題で繰り返し出てくる
