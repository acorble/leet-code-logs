"""125. Valid Palindrome のテスト。

`solution` フィクスチャは同じディレクトリの solution.py を読み込む。
英数字だけを見て、大文字小文字を区別せずに回文かどうかを判定する。
"""

import random
import string


def is_palindrome(solution, s):
    return solution.Solution().isPalindrome(s)


def brute_force(s):
    """英数字だけ抜き出して小文字にし、反転と比べる（正解の基準）。"""
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


def test_example_1(solution):
    assert is_palindrome(solution, "A man, a plan, a canal: Panama") is True


def test_example_2(solution):
    assert is_palindrome(solution, "race a car") is False


def test_example_3(solution):
    """空白だけ。英数字が 1 つも無いので回文とみなす。"""
    assert is_palindrome(solution, " ") is True


def test_empty(solution):
    assert is_palindrome(solution, "") is True


def test_single_char(solution):
    assert is_palindrome(solution, "a") is True
    assert is_palindrome(solution, ".") is True


def test_symbols_only(solution):
    assert is_palindrome(solution, ".,!?") is True


def test_digits(solution):
    assert is_palindrome(solution, "0P") is False
    assert is_palindrome(solution, "12321") is True
    assert is_palindrome(solution, "1a2") is False


def test_symbols_in_the_middle(solution):
    """記号が中央に集まっていても、飛ばして比較できるか。"""
    assert is_palindrome(solution, "ab,,,,ba") is True
    assert is_palindrome(solution, "ab,,,,ab") is False


def test_random_against_brute_force(solution):
    rng = random.Random(0)
    alphabet = "aAbB12 ,.:!"
    for _ in range(2000):
        s = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 14)))
        assert is_palindrome(solution, s) == brute_force(s), (s,)


def test_random_true_cases(solution):
    """回文になる文字列を作って、確実に True 側も試す。"""
    rng = random.Random(1)
    for _ in range(500):
        half = "".join(rng.choice(string.ascii_letters + string.digits)
                       for _ in range(rng.randint(0, 8)))
        middle = rng.choice(["", rng.choice(string.ascii_letters)])
        noise = lambda: "".join(rng.choice(" ,.!") for _ in range(rng.randint(0, 3)))
        s = noise().join([half, middle, half[::-1]])
        assert is_palindrome(solution, s) == brute_force(s), (s,)
