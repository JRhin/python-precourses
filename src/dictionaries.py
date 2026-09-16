"""Exercises: Dictionaries."""


def get_or_default(d: dict, key, default=None):
    """Return d[key] if present, otherwise return default.

    >>> get_or_default({"a": 1}, "a")
    1
    >>> get_or_default({"a": 1}, "b", "missing")
    'missing'
    """
    raise NotImplementedError("TODO: implement get_or_default")


def merge_dicts(a: dict, b: dict) -> dict:
    """Return a new dict combining a and b. If a key exists in both, b's
    value wins.

    >>> merge_dicts({"x": 1, "y": 2}, {"y": 3, "z": 4})
    {'x': 1, 'y': 3, 'z': 4}
    """
    raise NotImplementedError("TODO: implement merge_dicts")


def invert_dict(d: dict) -> dict:
    """Return a new dict with keys and values swapped. Assume all values in
    d are unique and hashable.

    >>> invert_dict({"a": 1, "b": 2})
    {1: 'a', 2: 'b'}
    """
    raise NotImplementedError("TODO: implement invert_dict")


def count_occurrences(items: list) -> dict:
    """Return a dict mapping each distinct item to how many times it
    appears in the list.

    >>> count_occurrences(["a", "b", "a", "c", "b", "a"])
    {'a': 3, 'b': 2, 'c': 1}
    """
    raise NotImplementedError("TODO: implement count_occurrences")


def group_by_length(words: list) -> dict:
    """Group words into a dict keyed by word length, mapping each length
    to the list of words (in original order) that have that length.

    >>> group_by_length(["a", "bb", "cc", "ddd"])
    {1: ['a'], 2: ['bb', 'cc'], 3: ['ddd']}
    """
    raise NotImplementedError("TODO: implement group_by_length")


def deep_get(d: dict, path: list, default=None):
    """Traverse nested dicts following the sequence of keys in path,
    e.g. deep_get(d, ["a", "b"]) is like d["a"]["b"], but returns default
    if any key along the way is missing (instead of raising KeyError).

    >>> deep_get({"a": {"b": 1}}, ["a", "b"])
    1
    >>> deep_get({"a": {"b": 1}}, ["a", "c"], "default")
    'default'
    """
    raise NotImplementedError("TODO: implement deep_get")
