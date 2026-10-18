"""271. Encode and Decode Strings のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
encode した文字列を decode すると、元のリストに戻ることを確かめる（encode の形式は自由）。
これまでの解答は Java（attempts/*.java）なので、Python の解答が入るまではスキップする。
"""

import pytest


def round_trip(solution, strs):
    s = solution.Solution()
    try:
        return s.decode(s.encode(strs))
    except NotImplementedError:
        pytest.skip("Python の解答はまだない（これまでの解答は attempts/*.java）")


def test_example_1(solution):
    strs = ["neet", "code", "love", "you"]
    assert round_trip(solution, strs) == strs


def test_example_2(solution):
    strs = ["we", "say", ":", "yes"]
    assert round_trip(solution, strs) == strs


def test_empty_list(solution):
    assert round_trip(solution, []) == []


def test_empty_strings(solution):
    assert round_trip(solution, ["", "", "a"]) == ["", "", "a"]


def test_long_string(solution):
    # 長さが 2 桁以上（10 文字以上）
    strs = ["abcdefghijk", "x" * 120]
    assert round_trip(solution, strs) == strs


def test_strings_containing_digits_and_symbols(solution):
    # 区切りに使いそうな文字や数字が、文字列の中に入っていても戻せる
    strs = ["4#neet", "12", "#", "a#b#"]
    assert round_trip(solution, strs) == strs
