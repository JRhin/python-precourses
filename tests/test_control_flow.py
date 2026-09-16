import pytest

from src.control_flow import bmi_category, classify_number, describe_day, fizzbuzz, grade_from_score


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, "positive"),
        (-5, "negative"),
        (0, "zero"),
        (0.1, "positive"),
        (-0.1, "negative"),
        (100, "positive"),
        (-100, "negative"),
        (0.0, "zero"),
        (1, "positive"),
        (-1, "negative"),
    ],
)
def test_classify_number(n, expected):
    assert classify_number(n) == expected


@pytest.mark.parametrize(
    "score, expected",
    [
        (95, "A"),
        (61, "D"),
        (40, "F"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (60, "D"),
    ],
)
def test_grade_from_score(score, expected):
    assert grade_from_score(score) == expected


@pytest.mark.parametrize(
    "day, expected",
    [
        ("Saturday", "Weekend!"),
        ("Monday", "Weekday"),
        ("Sunday", "Weekend!"),
        ("Tuesday", "Weekday"),
        ("Wednesday", "Weekday"),
        ("Thursday", "Weekday"),
        ("Friday", "Weekday"),
        ("Saturday", "Weekend!"),
        ("Sunday", "Weekend!"),
        ("Monday", "Weekday"),
    ],
)
def test_describe_day(day, expected):
    assert describe_day(day) == expected


@pytest.mark.parametrize(
    "weight_kg, height_m, expected",
    [
        (50, 1.75, "underweight"),
        (70, 1.75, "normal"),
        (90, 1.75, "overweight"),
        (100, 1.75, "obese"),
        (60, 1.60, "normal"),
        (45, 1.60, "underweight"),
        (80, 1.80, "normal"),
        (110, 1.80, "obese"),
        (65, 1.70, "normal"),
        (55, 1.65, "normal"),
    ],
)
def test_bmi_category(weight_kg, height_m, expected):
    assert bmi_category(weight_kg, height_m) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "1"),
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (2, "2"),
        (9, "Fizz"),
        (10, "Buzz"),
        (30, "FizzBuzz"),
        (7, "7"),
        (45, "FizzBuzz"),
    ],
)
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected
