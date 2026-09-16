import pytest

from src.dictionaries import count_occurrences, deep_get, get_or_default, group_by_length, invert_dict, merge_dicts


@pytest.mark.parametrize(
    "d, key, default, expected",
    [
        ({"a": 1}, "a", None, 1),
        ({"a": 1}, "b", "missing", "missing"),
        ({}, "x", 0, 0),
        ({"a": 1, "b": 2}, "b", None, 2),
        ({}, "a", "d", "d"),
        ({"x": None}, "x", "d", None),
        ({"a": 1}, "a", "d", 1),
        ({"k": 0}, "k", 99, 0),
        ({"a": 1, "b": 2}, "c", -1, -1),
        ({}, "z", [], []),
    ],
)
def test_get_or_default(d, key, default, expected):
    assert get_or_default(d, key, default) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ({"x": 1, "y": 2}, {"y": 3, "z": 4}, {"x": 1, "y": 3, "z": 4}),
        ({}, {"a": 1}, {"a": 1}),
        ({"a": 1}, {}, {"a": 1}),
        ({"a": 1}, {"a": 2}, {"a": 2}),
        ({"a": 1, "b": 2}, {"c": 3}, {"a": 1, "b": 2, "c": 3}),
        ({}, {}, {}),
        ({"x": 1}, {"y": 2}, {"x": 1, "y": 2}),
        ({"a": 1}, {"b": 2, "c": 3}, {"a": 1, "b": 2, "c": 3}),
        ({"k": 1, "v": 2}, {"v": 3}, {"k": 1, "v": 3}),
        ({"1": 1}, {"2": 2}, {"1": 1, "2": 2}),
    ],
)
def test_merge_dicts(a, b, expected):
    assert merge_dicts(a, b) == expected


@pytest.mark.parametrize(
    "d, expected",
    [
        ({"a": 1, "b": 2}, {1: "a", 2: "b"}),
        ({}, {}),
        ({"x": 1}, {1: "x"}),
        ({"a": 1, "b": 2, "c": 3}, {1: "a", 2: "b", 3: "c"}),
        ({"k": 0}, {0: "k"}),
        ({"one": 1, "two": 2, "three": 3}, {1: "one", 2: "two", 3: "three"}),
        ({"z": 26}, {26: "z"}),
        ({"a": 100}, {100: "a"}),
        ({"p": 1, "q": 2}, {1: "p", 2: "q"}),
        ({"m": -1}, {-1: "m"}),
    ],
)
def test_invert_dict(d, expected):
    assert invert_dict(d) == expected


@pytest.mark.parametrize(
    "items, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([], {}),
        (["x"], {"x": 1}),
        ([1, 1, 2, 2, 3], {1: 2, 2: 2, 3: 1}),
        (["a", "a", "a"], {"a": 3}),
        ([True, True, False], {True: 2, False: 1}),
        ([1, 2, 3], {1: 1, 2: 1, 3: 1}),
        (["x", "y", "x", "y", "x"], {"x": 3, "y": 2}),
        ([0, 0, 0, 1], {0: 3, 1: 1}),
        (["a", "b", "c"], {"a": 1, "b": 1, "c": 1}),
    ],
)
def test_count_occurrences(items, expected):
    assert count_occurrences(items) == expected


@pytest.mark.parametrize(
    "words, expected",
    [
        (["a", "bb", "cc", "ddd"], {1: ["a"], 2: ["bb", "cc"], 3: ["ddd"]}),
        ([], {}),
        (["x"], {1: ["x"]}),
        (["hi", "by", "ok"], {2: ["hi", "by", "ok"]}),
        (["a", "ab", "abc", "abcd"], {1: ["a"], 2: ["ab"], 3: ["abc"], 4: ["abcd"]}),
        (["cat", "dog", "fish"], {3: ["cat", "dog"], 4: ["fish"]}),
        (["one", "two", "three", "four"], {3: ["one", "two"], 5: ["three"], 4: ["four"]}),
        (["x", "yy", "zzz"], {1: ["x"], 2: ["yy"], 3: ["zzz"]}),
        (["aa", "bb"], {2: ["aa", "bb"]}),
        (["a", "aa", "aaa", "aaaa", "aaaaa"], {1: ["a"], 2: ["aa"], 3: ["aaa"], 4: ["aaaa"], 5: ["aaaaa"]}),
    ],
)
def test_group_by_length(words, expected):
    assert group_by_length(words) == expected


@pytest.mark.parametrize(
    "d, path, default, expected",
    [
        ({"a": {"b": 1}}, ["a", "b"], None, 1),
        ({"a": {"b": 1}}, ["a", "c"], "default", "default"),
        ({}, ["a"], "d", "d"),
        ({"a": 1}, ["a", "b"], "d", "d"),
        ({"x": {"y": {"z": 42}}}, ["x", "y", "z"], None, 42),
        ({"a": {"b": 2}}, ["a"], None, {"b": 2}),
        ({}, [], None, {}),
        ({"a": 1}, [], None, {"a": 1}),
        ({"a": {"b": {"c": 3}}}, ["a", "b", "c"], 0, 3),
        ({"a": {}}, ["a", "b"], "missing", "missing"),
    ],
)
def test_deep_get(d, path, default, expected):
    assert deep_get(d, path, default) == expected
