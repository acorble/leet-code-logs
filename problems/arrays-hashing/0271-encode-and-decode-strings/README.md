# 271. Encode and Decode Strings

- URL: https://neetcode.io/problems/string-encode-and-decode
- 難易度: medium
- カテゴリ: arrays-hashing
- 初回: 2026-06-01（日付は記憶による。NeetCode で解いた。LeetCode では Premium 限定）

## 復習ログ

<!-- ATTEMPTS:START -->

| 回 | 日付 | 結果 | 自力 | 所要時間 | コード | メモ |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-06-01 | - | ? | - | [attempts/2026-06-01.java](attempts/2026-06-01.java) | Java。各文字列の前に長さ（1 桁）を付けてつなぐ。Example で答えが合わない（後述） |

<!-- ATTEMPTS:END -->

## 次回やること

<!-- 次に解き直すときに試したいこと。`- [ ] ...` の形で書き、済んだら行ごと消す。本人も Claude も書いてよい -->

- [ ] Python で解く
- [ ] 長さと中身の間に区切り文字を入れる形（`4#neet`）にして、2 桁以上の長さでも戻せるようにする
- [ ] 提出前に、10 文字以上の文字列と空文字を自分で試す

## 問題の要約

文字列のリストを 1 本の文字列に変換する `encode` と、それを元のリストに戻す `decode` を作る。
文字列には**どんな文字でも**入りうるので、単純な区切り文字（`,` など）では戻せない。

## 考えたこと / アプローチ

<!-- ここは本人が手で書く欄。Claude は見出しだけ用意し、中身は書かない。 -->

### 1 回目

<!-- 最初に思いついた方針、詰まった点、気づき -->

## 計算量

n はすべての文字列の合計の長さ。

- 時間: **O(n²)**（encode）— Java の `String` は書き換えられないので、`concat` のたびに今までの全体をコピーし直す。
  `StringBuilder` を使えば O(n) になる。decode は O(n)
- 空間: **O(n)** — encode した文字列と、decode したリスト

## 学び・再利用できるパターン

### 1 回目のコードで起きること

手元で Java のまま Example を動かした結果:

| 入力 | decode の結果 | 原因 |
| --- | --- | --- |
| `["neet","code","love","you"]` | `["nee","cod","lov","yo"]` | 終わりの位置が 1 つ手前 |
| `["abcdefghijk"]`（11 文字） | `StringIndexOutOfBoundsException` | 長さを 1 桁と決めつけている |

**1. 終わりの位置が 1 つ手前**

```java
substring = str.substring(countedChar + 1, countedChar + numChar);
```

`countedChar` が長さの数字の位置、中身は `countedChar + 1` から `numChar` 文字。
`substring(begin, end)` の `end` は**含まない**ので、終わりは `countedChar + 1 + numChar` にする必要がある。
次の位置を進める `countedChar += 1 + numChar` のほうは正しく `1 +` が入っているので、ここだけずれている。

**2. 長さが 2 桁以上だと読めない**

`str.charAt(countedChar) - '0'` は**1 文字だけ**を数字として読む。
`"11abcdefghijk"` だと長さを `1` と読んでしまい、次の位置が全部ずれる。

### 長さの後ろに区切り文字を置く

長さが何桁あるか分からないので、**長さの終わりに区切り文字**を置く。

```
["neet", "a#b"]   →   "4#neet3#a#b"
```

decode では、`#` が見つかるまでを長さとして読み、そこから長さ分の文字をそのまま取る。
中身に `#` や数字が入っていても、**長さの分だけ読み飛ばす**ので混ざらない
（`test_strings_containing_digits_and_symbols` はこれを確かめている）。

区切り文字だけ（`"neet#a#b"` のような形）では、中身の `#` と区切りの `#` を見分けられない。
長さを先に書くことで、中身を「中身」として扱えるようになるのがこの方法の要点。

### 細かい点（Java）

- 文字列を `concat` でつなぎ続けると、毎回全体がコピーされて O(n²) になる。
  何度もつなぐときは `StringBuilder` の `append` を使う
- `decode` の中に `System.out.println` が残っている。NeetCode / LeetCode では標準出力も実行時間に効くので、提出前に消す
