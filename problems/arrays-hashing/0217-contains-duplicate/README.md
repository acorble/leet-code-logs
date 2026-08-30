# 217. Contains Duplicate

- URL: https://leetcode.com/problems/contains-duplicate/
- 難易度: easy
- カテゴリ: arrays-hashing
- 初回: 2026-08-16

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-08-16 | - | - | [solution.py](solution.py) | |

<!-- ATTEMPTS:END -->

## 問題の要約

配列に同じ値が 2 回以上現れるなら True、すべて異なるなら False を返す。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

## 計算量

- 時間: O(n)
- 空間: O(n)

## 学び・再利用できるパターン

- 「既出かどうか」だけを知りたいなら dict ではなく set で足りる。
  インデックスや個数が要るなら dict になる（[Two Sum](../0001-two-sum) は dict）
- `len(set(nums)) != len(nums)` でも 1 行で書けるが、常に全要素を見る。
  早期 return できるぶん、走査しながら判定するほうが実際には速い場合がある
