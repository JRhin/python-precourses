"""Exercises: Strings."""


def reverse_string(s: str) -> str:
    """Return s reversed.

    >>> reverse_string("Hello")
    'olleH'
    """
    raise NotImplementedError("TODO: implement reverse_string")


def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards
    (case-insensitive). Assume no spaces/punctuation to worry about.

    >>> is_palindrome("level")
    True
    >>> is_palindrome("Level")
    True
    >>> is_palindrome("hello")
    False
    """
    raise NotImplementedError("TODO: implement is_palindrome")


def count_vowels(s: str) -> int:
    """Return how many vowels (a, e, i, o, u, case-insensitive) are in s.

    >>> count_vowels("Hello World")
    3
    """
    raise NotImplementedError("TODO: implement count_vowels")


def title_case_words(s: str) -> str:
    """Return s with the first letter of every word capitalized and the
    rest of each word unchanged. Do NOT use str.title(): it mishandles
    words that already contain uppercase letters.

    >>> title_case_words("the quick brown fox")
    'The Quick Brown Fox'
    >>> title_case_words("PYTHON is fun")
    'PYTHON Is Fun'
    """
    raise NotImplementedError("TODO: implement title_case_words")


def format_greeting(name: str, age: int) -> str:
    """Return a friendly one-line greeting combining name and age.

    >>> format_greeting("Pippo", 25)
    "Hi, I'm Pippo and I'm 25 years old!"
    """
    raise NotImplementedError("TODO: implement format_greeting")


def is_anagram(a: str, b: str) -> bool:
    """Return True if a and b are anagrams of each other: they contain
    exactly the same letters (ignoring case and spaces), just possibly in
    a different order.

    >>> is_anagram("listen", "silent")
    True
    >>> is_anagram("hello", "world")
    False
    """
    raise NotImplementedError("TODO: implement is_anagram")


def run_length_encode(s: str) -> str:
    """Return the run-length encoding of s: each run of identical
    consecutive characters becomes "<char><count>".

    >>> run_length_encode("aaabbc")
    'a3b2c1'
    >>> run_length_encode("abc")
    'a1b1c1'
    """
    raise NotImplementedError("TODO: implement run_length_encode")
