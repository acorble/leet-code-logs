# 定型句集

面接の流れの順に並べている。`n` や `h` は問題に合わせて読み替える。

## 1. 問題を確認する

| 言い回し | 使う場面・メモ | 出典 |
| --- | --- | --- |
| "Let me repeat the problem statement to make sure I understand it." | 最初の一言。問題を自分の言葉で言い直す前置き | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "Before I move on to the plan, let me ask a few clarifying questions." | 方針に入る前に質問する宣言。move on の後ろに **to** | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "Can the input be empty? I mean, can the root be None?" | 空の入力の確認。"be just None" より "empty" のほうが伝わる | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "The tree isn't necessarily balanced, so I'll assume it can be skewed." | 「〜とは限らない」は **not necessarily** | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "I assume the values don't affect the result, so I'll just ..." | 質問で時間を使うより、**仮定を言い切って進む**。違っていれば面接官が止めてくれる | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "I think I understand the problem now." | 確認を終える合図。"I can understand correctly the problem" としない | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |

## 2. 方針を話す

| 言い回し | 使う場面・メモ | 出典 |
| --- | --- | --- |
| "There are two approaches: X and Y. I'll go with X since ... Y would also work, but ..." | 選択肢を示し、**選んだ理由とトレードオフを 1 文で**添える | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "I'll go with recursive DFS since it's the simplest to write. BFS with a queue would also work and avoids deep recursion." | 上の型の木の問題での例 | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "Shall I go ahead and code it?" / "Can I move on to the implementation?" | 実装に入ってよいかの確認 | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |

## 3. 書きながら話す

| 言い回し | 使う場面・メモ | 出典 |
| --- | --- | --- |
| "Let me outline the structure first. First, the base case. Then, ... Finally, ..." | 各行に入る前に**骨組みを先に言う**。聞き手がどの行の話か追いやすくなる | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "If the root is None, these two lines would throw an error, so I need a base case." | ベースケースの理由。error は名詞なので "be error" ではなく **throw an error** / **would fail** | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "I'll call this function twice: once for each child." | "two times twice" と重ねない | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "Should I write it inside the Solution class, like on LeetCode?" | 関数のシグネチャの形を確認する | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |

## 4. 書いたコードを確かめる

| 言い回し | 使う場面・メモ | 出典 |
| --- | --- | --- |
| "Let me walk through a small example." | 書き終えたら計算量の前にこれ。"I think this can work correctly" で終わらせない | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "Let me also check the edge cases: an empty input, and ..." | 最初の確認で挙げたケースをここで使い回す | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |

## 5. 計算量を言う

| 言い回し | 使う場面・メモ | 出典 |
| --- | --- | --- |
| "Time is O(n), where n is the number of nodes, because we visit each node exactly once." | 「where n **is** ...」。"where N it's" としない | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "Space is O(h), where h is the height of the tree, because of the recursion stack. That's O(log n) for a balanced tree and O(n) in the worst case, when the tree is skewed like a linked list." | 再帰で木を降りる問題の空間計算量。**最初からこの形で一息に言う** | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "Each call uses constant space, and there can be up to n calls on the stack at the same time." | 再帰の空間計算量の根拠 | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "The recursion depth is n." | depth は単数。"the depths of the recursion is" としない | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |

## 6. やりとり

| 言い回し | 使う場面・メモ | 出典 |
| --- | --- | --- |
| "Sorry, I'm not sure I follow. Do you mean ...?" | 聞き取れなかったとき。自分の理解を添えると相手が説明し直しやすい。"repeat that again" の again は不要 | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "Let me think for a second." | 考える間を取る。"So, uh..." でつなぐ代わりに | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "If I'm not mistaken, ..." | 自信がないときの前置き。"If I'm not wrong" も通じるが、こちらが決まった言い方。ただし計算量のように根拠を言える場面では、前置きより根拠を言い切るほうが強い | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "Do you have any questions or comments?" | 説明を終えて相手に渡す。226 でできていた | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |

## 自分の癖（注意する語）

レビューで繰り返し指摘されたもの。

| 癖 | 正しくは | 出典 |
| --- | --- | --- |
| problem を "program" と言う（または program に聞こえる） | problem /ˈprɑːbləm/。program /ˈproʊɡræm/ と区別する | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| 単数・複数、三人称単数（"3 case", "they has both child"） | three **cases** / it **has** both **children** | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| 文頭がほぼ毎回 "So, uh" | 黙って間を取るか "Let me think for a second." | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
| "binary" だけで名詞にする（"the given binary is not balanced"） | **binary tree** まで言う | [226](../problems/trees/0226-invert-binary-tree/english/2026-09-19-mock.md) |
