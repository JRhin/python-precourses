import pytest

from src.tuples import first_and_last, make_point, nested_tuple_sum, pairs_to_dict, swap_tuple, unzip


@pytest.mark.parametrize(
    "t, expected",
    [
        ((1, 2), (2, 1)),
        ((3, 4), (4, 3)),
        (("a", "b"), ("b", "a")),
        ((0, 0), (0, 0)),
        ((True, False), (False, True)),
        ((1.5, 2.5), (2.5, 1.5)),
        (("x", "y"), ("y", "x")),
        ((-1, 1), (1, -1)),
        ((100, 200), (200, 100)),
        ((None, 1), (1, None)),
    ],
)
def test_swap_tuple(t, expected):
    assert swap_tuple(t) == expected


@pytest.mark.parametrize(
    "t, expected",
    [
        ((10, 20, 30, 40), (10, 40)),
        ((1, 2), (1, 2)),
        ((5,), (5, 5)),
        ((1, 2, 3), (1, 3)),
        (("a", "b", "c"), ("a", "c")),
        ((0, 0, 0), (0, 0)),
        ((1, 2, 3, 4, 5), (1, 5)),
        ((True, False), (True, False)),
        ((-1, -2, -3), (-1, -3)),
        ((9, 8, 7, 6, 5), (9, 5)),
    ],
)
def test_first_and_last(t, expected):
    assert first_and_last(t) == expected


@pytest.mark.parametrize(
    "pairs, expected",
    [
        ([("a", 1), ("b", 2)], {"a": 1, "b": 2}),
        ([], {}),
        ([("x", 1)], {"x": 1}),
        ([("a", 1), ("a", 2)], {"a": 2}),
        ([(1, "one"), (2, "two")], {1: "one", 2: "two"}),
        ([("k", None)], {"k": None}),
        ([(True, 1), (False, 0)], {True: 1, False: 0}),
        ([("a", 1), ("b", 2), ("c", 3)], {"a": 1, "b": 2, "c": 3}),
        ([(1, 1)], {1: 1}),
        ([("z", 26)], {"z": 26}),
    ],
)
def test_pairs_to_dict(pairs, expected):
    assert pairs_to_dict(pairs) == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, (1, 2)),
        (0, 0, (0, 0)),
        (-1, -2, (-1, -2)),
        (3.5, 4.5, (3.5, 4.5)),
        (100, 200, (100, 200)),
        (-5, 5, (-5, 5)),
        (1, 1, (1, 1)),
        (0, 5, (0, 5)),
        (5, 0, (5, 0)),
        (2.2, 3.3, (2.2, 3.3)),
    ],
)
def test_make_point(x, y, expected):
    assert make_point(x, y) == expected
    assert isinstance(make_point(x, y), tuple)


@pytest.mark.parametrize(
    "pairs, expected",
    [
        ([(1, "a"), (2, "b"), (3, "c")], ([1, 2, 3], ["a", "b", "c"])),
        ([(1, 2)], ([1], [2])),
        ([("x", 1), ("y", 2)], (["x", "y"], [1, 2])),
        ([(1, 1), (2, 2), (3, 3)], ([1, 2, 3], [1, 2, 3])),
        ([(True, 1), (False, 0)], ([True, False], [1, 0])),
        ([(0, 0)], ([0], [0])),
        ([("a", 1), ("b", 2), ("c", 3), ("d", 4)], (["a", "b", "c", "d"], [1, 2, 3, 4])),
        ([(1, "one")], ([1], ["one"])),
        ([(5, 6)], ([5], [6])),
        ([(1, 2), (3, 4), (5, 6)], ([1, 3, 5], [2, 4, 6])),
    ],
)
def test_unzip(pairs, expected):
    assert unzip(pairs) == expected


@pytest.mark.parametrize(
    "t, expected",
    [
        ((1, 2, 3), 6),
        ((1, (2, 3), 4), 10),
        (((1, 2), (3, 4)), 10),
        ((1, (2, (3, 4))), 10),
        ((1, 2, 3, 4), 10),
        ((1,), 1),
        ((1, (2, (3, (4, 5)))), 15),
        ((5, 5, 5), 15),
        (((1,), (2,), (3,)), 6),
        ((1, 2, (3, (4, (5, 6)))), 21),
    ],
)
def test_nested_tuple_sum(t, expected):
    assert nested_tuple_sum(t) == expected
