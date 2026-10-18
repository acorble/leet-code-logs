# 解き直しの予定

このファイルは `python scripts/update_review.py` で自動生成される。**手で編集しない。**
各問題の README の「復習ログ」と「次回やること」から作っている（2026-10-18 時点）。

## 間隔の決め方

何も見ずに解けるたびに間隔を広げる: 3 日 → 7 日 → 14 日 → 30 日 → 60 日 → 卒業

| 自力 | 意味 | 次の間隔 |
| --- | --- | --- |
| ◎ | 何も見ずにすんなり解けた | 1 段広げる |
| ○ | 何も見ずに解けたが時間がかかった | 据え置き（最低 1 週間） |
| △ | ヒント・過去の解答・解説を見た | 3 日に戻す |
| × | 解けなかった | 3 日に戻す |
| ? | 記録なし | ○ と同じに扱う |

同じ日の 2 回目以降（直後の書き直し）は数えない。
期限切れは「間隔に対してどれだけ遅れているか」の割合が大きい順に並べている。

## 今週やる (5)

| 問題 | 前回 | 自力の履歴 | 間隔 | 予定日 | 状態 | 次回やること |
| --- | --- | --- | --- | --- | --- | --- |
| [543. Diameter of Binary Tree](problems/trees/0543-diameter-of-binary-tree) | 2026-07-28 | △ | 3 日 | 2026-07-31 | **79 日超過** | 深さを下から持ち上げる DFS で O(n) に解き直す<br>NeetCode の解説動画を見る |
| [49. Group Anagrams](problems/arrays-hashing/0049-group-anagrams) | 2026-05-23 | ? → ? | 7 日 | 2026-05-30 | **141 日超過** | Python で解く<br>「26 文字分の個数」をキーにする版で書く（キーを作るのが O(k log k) から O(k) になる。1 回目のコメントの「int[] でもやってみたい」） |
| [347. Top K Frequent Elements](problems/arrays-hashing/0347-top-k-frequent-elements) | 2026-05-30 | ? | 7 日 | 2026-06-06 | **134 日超過** | Python で解く<br>並べ替えを使わずに O(n) で解く（「出現回数」を添え字にしたバケツを使う） |
| [271. Encode and Decode Strings](problems/arrays-hashing/0271-encode-and-decode-strings) | 2026-06-01 | ? | 7 日 | 2026-06-08 | **132 日超過** | Python で解く<br>長さと中身の間に区切り文字を入れる形（`4#neet`）にして、2 桁以上の長さでも戻せるようにする<br>提出前に、10 文字以上の文字列と空文字を自分で試す |
| [238. Product of Array Except Self](problems/arrays-hashing/0238-product-of-array-except-self) | 2026-06-03 | ? | 7 日 | 2026-06-10 | **130 日超過** | Python で解く<br>follow-up: `prefixes` / `suffixes` の配列を使わず、答えの配列だけで解く（追加の空間 O(1)） |

## 期限切れ（残り 33）

| 問題 | 前回 | 自力の履歴 | 間隔 | 予定日 | 状態 | 次回やること |
| --- | --- | --- | --- | --- | --- | --- |
| [36. Valid Sudoku](problems/arrays-hashing/0036-valid-sudoku) | 2026-06-04 | ? | 7 日 | 2026-06-11 | **129 日超過** | Python で解く<br>盤面を 1 周するだけで、行・列・ブロックを同時にチェックする（ブロックの番号は `(r // 3, c // 3)`） |
| [128. Longest Consecutive Sequence](problems/arrays-hashing/0128-longest-consecutive-sequence) | 2026-06-05 | ? | 7 日 | 2026-06-12 | **128 日超過** | O(n) で解く（毎回 `Collections.min` で最小値を探さずに、どこから数え始めればよいかを考える）<br>Python で解く |
| [167. Two Sum II - Input Array Is Sorted](problems/two-pointers/0167-two-sum-ii-input-array-is-sorted) | 2026-06-11 | ? | 7 日 | 2026-06-18 | **122 日超過** | なぜ「小さければ左、大きければ右」を動かしても答えを飛ばさないのか、自分の言葉で説明できるようにする |
| [11. Container With Most Water](problems/two-pointers/0011-container-with-most-water) | 2026-06-13 | ? | 7 日 | 2026-06-20 | **120 日超過** | 左右で同じ処理を 2 回書かずに、「低いほうを 1 つ動かす」1 本のループで書く<br>なぜ低いほうを動かせばよいのか（高いほうを動かしても増えない理由）を説明できるようにする |
| [121. Best Time to Buy and Sell Stock](problems/sliding-window/0121-best-time-to-buy-and-sell-stock) | 2026-06-15 | ? | 7 日 | 2026-06-22 | **118 日超過** |  |
| [3. Longest Substring Without Repeating Characters](problems/sliding-window/0003-longest-substring-without-repeating-characters) | 2026-06-16 | ? | 7 日 | 2026-06-23 | **117 日超過** | 同じ情報を 2 通りの方法で求めていないか見直す（`left + i` で足りる） |
| [424. Longest Repeating Character Replacement](problems/sliding-window/0424-longest-repeating-character-replacement) | 2026-06-17 | ? | 7 日 | 2026-06-24 | **116 日超過** |  |
| [155. Min Stack](problems/stack/0155-min-stack) | 2026-06-21 | ? | 7 日 | 2026-06-28 | **112 日超過** | Stack を 1 本にして、`(値, その時点の最小値)` の組を積む形で書く |
| [704. Binary Search](problems/binary-search/0704-binary-search) | 2026-06-24 | ? | 7 日 | 2026-07-01 | **109 日超過** |  |
| [74. Search a 2D Matrix](problems/binary-search/0074-search-a-2d-matrix) | 2026-06-26 | ? | 7 日 | 2026-07-03 | **107 日超過** |  |
| [875. Koko Eating Bananas](problems/binary-search/0875-koko-eating-bananas) | 2026-06-27 | ? | 7 日 | 2026-07-04 | **106 日超過** |  |
| [153. Find Minimum in Rotated Sorted Array](problems/binary-search/0153-find-minimum-in-rotated-sorted-array) | 2026-06-28 | ? | 7 日 | 2026-07-05 | **105 日超過** |  |
| [981. Time Based Key-Value Store](problems/binary-search/0981-time-based-key-value-store) | 2026-06-30 | ? | 7 日 | 2026-07-07 | **103 日超過** | `sort()` が本当に必要か考え直す<br>dict を key → [(timestamp, value)] の 1 本にまとめる |
| [21. Merge Two Sorted Lists](problems/linked-list/0021-merge-two-sorted-lists) | 2026-07-04 | ? | 7 日 | 2026-07-11 | **99 日超過** |  |
| [206. Reverse Linked List](problems/linked-list/0206-reverse-linked-list) | 2026-07-04 | ? → ? | 7 日 | 2026-07-11 | **99 日超過** |  |
| [141. Linked List Cycle](problems/linked-list/0141-linked-list-cycle) | 2026-07-10 | ? → ? | 7 日 | 2026-07-17 | **93 日超過** | ループ条件を標準形 `while fast and fast.next` で書く |
| [1. Two Sum](problems/arrays-hashing/0001-two-sum) | 2026-07-11 | ? | 7 日 | 2026-07-18 | **92 日超過** |  |
| [143. Reorder List](problems/linked-list/0143-reorder-list) | 2026-07-11 | ? → ? | 7 日 | 2026-07-18 | **92 日超過** |  |
| [104. Maximum Depth of Binary Tree](problems/trees/0104-maximum-depth-of-binary-tree) | 2026-07-23 | ? | 7 日 | 2026-07-30 | **80 日超過** | Stack を使った Iterative DFS で解く |
| [567. Permutation in String](problems/sliding-window/0567-permutation-in-string) | 2026-08-03 | ? | 7 日 | 2026-08-10 | **69 日超過** |  |
| [125. Valid Palindrome](problems/two-pointers/0125-valid-palindrome) | 2026-08-16 | ? → ? → ? | 7 日 | 2026-08-23 | **56 日超過** | 内側の while にも `l < r` を入れる。提出前に、記号だけの文字列（`".,"`）を自分で試す<br>`isalnum()` / `lower()` を使わずに、文字コードの範囲（`'a' <= c <= 'z'` など）で判定して書いてみる（面接でよく聞かれる） |
| [226. Invert Binary Tree](problems/trees/0226-invert-binary-tree) | 2026-08-19 | ? → ? | 7 日 | 2026-08-26 | **53 日超過** |  |
| [110. Balanced Binary Tree](problems/trees/0110-balanced-binary-tree) | 2026-08-22 | ○ | 7 日 | 2026-08-29 | **50 日超過** | 返り値のタプルか外側の変数か、どちらか一方に寄せて書き直す |
| [100. Same Tree](problems/trees/0100-same-tree) | 2026-08-26 | ◎ | 7 日 | 2026-09-02 | **46 日超過** | BFS / Iterative DFS で解く |
| [572. Subtree of Another Tree](problems/trees/0572-subtree-of-another-tree) | 2026-08-28 | ○ | 7 日 | 2026-09-04 | **44 日超過** | 解答を見て、より良いやり方を確認する |
| [235. Lowest Common Ancestor of a Binary Search Tree](problems/trees/0235-lowest-common-ancestor-of-a-binary-search-tree) | 2026-08-29 | ? | 7 日 | 2026-09-05 | **43 日超過** | BST の大小関係で、探索する枝を片側に絞る |
| [102. Binary Tree Level Order Traversal](problems/trees/0102-binary-tree-level-order-traversal) | 2026-08-30 | ○ | 7 日 | 2026-09-06 | **42 日超過** |  |
| [1448. Count Good Nodes in Binary Tree](problems/trees/1448-count-good-nodes-in-binary-tree) | 2026-09-03 | ○ | 7 日 | 2026-09-10 | **38 日超過** | 経路の最大値だけを引数で渡して O(n) にする |
| [15. 3Sum](problems/two-pointers/0015-3sum) | 2026-09-06 | ? → ? | 7 日 | 2026-09-13 | **35 日超過** | 1 回目の「並べ替えて 1 つ固定 → 2 ポインタ」を、1 回目のコードを見ずに書く<br>ループの中の `print` を消して提出する<br>`nums[i] > 0` になったら、それ以降は 0 にならないので `break` する |
| [98. Validate Binary Search Tree](problems/trees/0098-validate-binary-search-tree) | 2026-09-07 | ○ | 7 日 | 2026-09-14 | **34 日超過** | 解説を見る<br>上から範囲 (low, high) を渡す別解で書く |
| [230. Kth Smallest Element in a BST](problems/trees/0230-kth-smallest-element-in-a-bst) | 2026-09-12 | ? | 7 日 | 2026-09-19 | **29 日超過** | 中順走査にして sort をなくす（O(n)）<br>k 個目で打ち切る（O(h + k)） |
| [199. Binary Tree Right Side View](problems/trees/0199-binary-tree-right-side-view) | 2026-10-09 | ◎ → △ | 3 日 | 2026-10-12 | **6 日超過** | 何も見ずに BFS 版を書く<br>DFS 版（右の子から潜り、各深さで最初に会ったノードを取る）を書く |
| [145. Binary Tree Postorder Traversal](problems/trees/0145-binary-tree-postorder-traversal) | 2026-10-10 | ◎ | 7 日 | 2026-10-17 | **1 日超過** | 再帰を使わず、スタックで解く（follow-up） |

## 今後の予定 (5)

| 問題 | 前回 | 自力の履歴 | 間隔 | 予定日 | 状態 | 次回やること |
| --- | --- | --- | --- | --- | --- | --- |
| [150. Evaluate Reverse Polish Notation](problems/stack/0150-evaluate-reverse-polish-notation) | 2026-10-18 | ○ → △ | 3 日 | 2026-10-21 | あと 3 日 | 動画を見ずに Stack で書けるか確かめる<br>演算子ごとの if 分岐を、演算子 → 関数の dict にまとめて書いてみる |
| [739. Daily Temperatures](problems/stack/0739-daily-temperatures) | 2026-10-15 | ○ | 7 日 | 2026-10-22 | あと 4 日 | Stack を使った O(n) の解法を自分で考える<br>提出前に `print` を消す |
| [20. Valid Parentheses](problems/stack/0020-valid-parentheses) | 2026-10-17 | ? → ? → ◎ | 14 日 | 2026-10-31 | あと 13 日 | 閉じ括弧 → 開き括弧の dict を使って、括弧ごとの if 分岐をなくして書く |
| [217. Contains Duplicate](problems/arrays-hashing/0217-contains-duplicate) | 2026-10-18 | ? → ◎ | 14 日 | 2026-11-01 | あと 14 日 |  |
| [242. Valid Anagram](problems/arrays-hashing/0242-valid-anagram) | 2026-10-18 | ? → ? → ◎ | 14 日 | 2026-11-01 | あと 14 日 | dict を 1 つにして、`s` は +1・`t` は -1 で数える形で書く。そのあと `collections.Counter` でも書いてみる |
