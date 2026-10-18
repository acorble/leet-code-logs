"""49. Group Anagrams のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
グループの順番も、グループ内の順番も問わないので、両方を並べ替えてから比べる。
これまでの解答は Java（attempts/*.java）なので、Python の解答が入るまではスキップする。
"""

import pytest


def group(solution, strs):
    try:
        result = solution.Solution().groupAnagrams(strs)
    except NotImplementedError:
        pytest.skip("Python の解答はまだない（これまでの解答は attempts/*.java）")
    return sorted(sorted(g) for g in result)


def test_example_1(solution):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert group(solution, strs) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_example_2(solution):
    assert group(solution, [""]) == [[""]]


def test_example_3(solution):
    assert group(solution, ["a"]) == [["a"]]


def test_empty_strings_group_together(solution):
    assert group(solution, ["", "", "b"]) == [["", ""], ["b"]]


def test_same_letters_different_counts(solution):
    # 文字の種類が同じでも個数が違えば別グループ
    assert group(solution, ["aab", "abb", "bab"]) == [["aab"], ["abb", "bab"]]
