import pytest

from src.variables_types import (
    describe_person,
    get_type_name,
    is_same_type,
    most_common_type,
    swap_values,
)


@pytest.mark.parametrize(
    "value, expected",
    [
        (10, "int"),
        ("hi", "str"),
        (3.14, "float"),
        (True, "bool"),
        ([1, 2], "list"),
        ((1, 2), "tuple"),
        ({1: 2}, "dict"),
        (None, "NoneType"),
        ({1, 2}, "set"),
        (b"x", "bytes"),
    ],
)
def test_get_type_name(value, expected):
    assert get_type_name(value) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, (2, 1)),
        (3, 4, (4, 3)),
        ("a", "b", ("b", "a")),
        (True, False, (False, True)),
        (1.5, 2.5, (2.5, 1.5)),
        (0, 0, (0, 0)),
        ([1], [2], ([2], [1])),
        ("x", 1, (1, "x")),
        (None, 1, (1, None)),
        ((1,), (2,), ((2,), (1,))),
    ],
)
def test_swap_values(a, b, expected):
    assert swap_values(a, b) == expected


@pytest.mark.parametrize(
    "name, age, height_in_m, is_student, expected",
    [
        ("Pippo", 25, 1.75, True, "Pippo is 25 years old, 1.75m tall, and is a student: True."),
        ("Anna", 30, 1.6, False, "Anna is 30 years old, 1.6m tall, and is a student: False."),
        ("Luca", 18, 1.8, True, "Luca is 18 years old, 1.8m tall, and is a student: True."),
        ("Maria", 45, 1.65, False, "Maria is 45 years old, 1.65m tall, and is a student: False."),
        ("Bob", 22, 1.9, True, "Bob is 22 years old, 1.9m tall, and is a student: True."),
        ("Ella", 60, 1.55, False, "Ella is 60 years old, 1.55m tall, and is a student: False."),
        ("Sam", 33, 1.72, True, "Sam is 33 years old, 1.72m tall, and is a student: True."),
        ("Zoe", 27, 1.68, False, "Zoe is 27 years old, 1.68m tall, and is a student: False."),
        ("Max", 50, 1.85, True, "Max is 50 years old, 1.85m tall, and is a student: True."),
        ("Lea", 40, 1.58, False, "Lea is 40 years old, 1.58m tall, and is a student: False."),
    ],
)
def test_describe_person(name, age, height_in_m, is_student, expected):
    assert describe_person(name, age, height_in_m, is_student) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, True),
        (1, True, False),
        (1.0, 1, False),
        ("a", "b", True),
        ([1], [2], True),
        ((1,), (2,), True),
        ({1: 1}, {2: 2}, True),
        (None, None, True),
        (True, True, True),
        (1.0, 2.0, True),
    ],
)
def test_is_same_type(a, b, expected):
    assert is_same_type(a, b) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, "a"], "int"),
        (["a", "b", 1], "str"),
        ([1, 2, 3, "x"], "int"),
        ([True, False, 1], "bool"),
        ([1.0, 2.0, "a", "b"], "float"),
        ([[1], [2], 1], "list"),
        ([{1: 1}, {2: 2}, 1], "dict"),
        ([(1,), (2,), 1], "tuple"),
        (["a", "a", "a", 1, 2], "str"),
        ([None, None, 1], "NoneType"),
    ],
)
def test_most_common_type(values, expected):
    assert most_common_type(values) == expected
