import pytest

from src.strings import (
    count_vowels,
    format_greeting,
    is_anagram,
    is_palindrome,
    reverse_string,
    run_length_encode,
    title_case_words,
)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello", "olleH"),
        ("", ""),
        ("a", "a"),
        ("ab", "ba"),
        ("racecar", "racecar"),
        ("Python", "nohtyP"),
        ("12345", "54321"),
        ("A man", "nam A"),
        ("  hi  ", "  ih  "),
        ("xyz", "zyx"),
    ],
)
def test_reverse_string(s, expected):
    assert reverse_string(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("level", True),
        ("Level", True),
        ("hello", False),
        ("a", True),
        ("", True),
        ("noon", True),
        ("Noon", True),
        ("abcba", True),
        ("abcda", False),
        ("Aa", True),
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello World", 3),
        ("", 0),
        ("xyz", 0),
        ("AEIOU", 5),
        ("aeiou", 5),
        ("Python Programming", 4),
        ("sky", 0),
        ("banana", 3),
        ("QUICK", 2),
        ("Umbrella", 3),
    ],
)
def test_count_vowels(s, expected):
    assert count_vowels(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("the quick brown fox", "The Quick Brown Fox"),
        ("hello", "Hello"),
        ("a b c", "A B C"),
        ("PYTHON is fun", "PYTHON Is Fun"),
        ("one", "One"),
        ("  ", ""),
        ("x y", "X Y"),
        ("hi there world", "Hi There World"),
        ("already Title", "Already Title"),
        ("single", "Single"),
    ],
)
def test_title_case_words(s, expected):
    assert title_case_words(s) == expected


@pytest.mark.parametrize(
    "name, age, expected",
    [
        ("Pippo", 25, "Hi, I'm Pippo and I'm 25 years old!"),
        ("Anna", 30, "Hi, I'm Anna and I'm 30 years old!"),
        ("Bob", 1, "Hi, I'm Bob and I'm 1 years old!"),
        ("Zoe", 99, "Hi, I'm Zoe and I'm 99 years old!"),
        ("X", 0, "Hi, I'm X and I'm 0 years old!"),
        ("Sam", 45, "Hi, I'm Sam and I'm 45 years old!"),
        ("Lea", 18, "Hi, I'm Lea and I'm 18 years old!"),
        ("Max", 60, "Hi, I'm Max and I'm 60 years old!"),
        ("Ivy", 33, "Hi, I'm Ivy and I'm 33 years old!"),
        ("Kay", 21, "Hi, I'm Kay and I'm 21 years old!"),
    ],
)
def test_format_greeting(name, age, expected):
    assert format_greeting(name, age) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("Dormitory", "Dirty Room", True),
        ("abc", "cab", True),
        ("abc", "abcd", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("Astronomer", "Moon starer", True),
        ("abc", "abd", False),
    ],
)
def test_is_anagram(a, b, expected):
    assert is_anagram(a, b) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aaabbc", "a3b2c1"),
        ("abc", "a1b1c1"),
        ("", ""),
        ("aaaa", "a4"),
        ("aabbcc", "a2b2c2"),
        ("x", "x1"),
        ("aabccc", "a2b1c3"),
        ("zzzzzzzzzz", "z10"),
        ("ab", "a1b1"),
        ("aabbbaa", "a2b3a2"),
    ],
)
def test_run_length_encode(s, expected):
    assert run_length_encode(s) == expected
