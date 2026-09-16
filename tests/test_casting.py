import pytest

from src.casting import celsius_to_fahrenheit, parse_bool, parse_csv_row, safe_cast_all, to_int_safe


@pytest.mark.parametrize(
    "s, default, expected",
    [
        ("42", 0, 42),
        ("not a number", -1, -1),
        ("-7", 0, -7),
        ("3.5", 0, 0),
        ("", 0, 0),
        ("007", 0, 7),
        ("  8  ", 0, 8),
        ("abc", 99, 99),
        ("0", 5, 0),
        ("100", -100, 100),
    ],
)
def test_to_int_safe(s, default, expected):
    assert to_int_safe(s, default) == expected


@pytest.mark.parametrize(
    "celsius, expected",
    [
        ("0", 32.0),
        ("100", 212.0),
        ("37", 98.6),
        ("-40", -40.0),
        ("20", 68.0),
        ("-273.15", -459.67),
        ("98.6", 209.48),
        ("25", 77.0),
        ("-10", 14.0),
        ("1000", 1832.0),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("true", True),
        ("False", False),
        ("TRUE", True),
        ("false", False),
        ("True", True),
        ("fAlSe", False),
        ("true", True),
        ("False", False),
        ("TRUE", True),
        ("false", False),
    ],
)
def test_parse_bool(s, expected):
    assert parse_bool(s) is expected


@pytest.mark.parametrize(
    "row, expected",
    [
        ("1,2.5,hello", [1, 2.5, "hello"]),
        ("a,b,c", ["a", "b", "c"]),
        ("1,2,3", [1, 2, 3]),
        ("1.1,2.2,3.3", [1.1, 2.2, 3.3]),
        ("x,1,2.5", ["x", 1, 2.5]),
        ("", [""]),
        ("5", [5]),
        ("1.0,2", [1.0, 2]),
        ("true,1,hello", ["true", 1, "hello"]),
        (" 1 , 2 , x ", [1, 2, "x"]),
    ],
)
def test_parse_csv_row(row, expected):
    assert parse_csv_row(row) == expected


@pytest.mark.parametrize(
    "values, target_type, expected",
    [
        (["1", "2", "x"], int, [1, 2]),
        (["1.5", "abc", "2.5"], float, [1.5, 2.5]),
        ([1, 2, 3], str, ["1", "2", "3"]),
        (["true", "1", ""], bool, [True, True, False]),
        (["1", "2", "3"], int, [1, 2, 3]),
        ([], int, []),
        (["a", "b"], int, []),
        (["1", "2.5", "3"], float, [1.0, 2.5, 3.0]),
        ([None, "1"], int, [1]),
        (["1", "-2", "3.5"], int, [1, -2]),
    ],
)
def test_safe_cast_all(values, target_type, expected):
    assert safe_cast_all(values, target_type) == expected
