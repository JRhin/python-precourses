import pytest

from src.error_handling import (
    NegativeValueError,
    divide_with_report,
    require_non_negative,
    retry,
    safe_int,
    validate_age,
    validate_password,
)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("42", 42),
        ("nope", None),
        ("-5", -5),
        ("3.5", None),
        ("", None),
        ("abc", None),
        ("007", 7),
        ("  8  ", 8),
        ("1e3", None),
        ("0", 0),
    ],
)
def test_safe_int(s, expected):
    assert safe_int(s) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(5, 5), (0, 0), (100, 100), (1000, 1000), (0.001, 0.001), (50, 50)],
)
def test_require_non_negative_valid(n, expected):
    assert require_non_negative(n) == expected


@pytest.mark.parametrize("n", [-1, -0.5, -1000, -0.001])
def test_require_non_negative_raises(n):
    with pytest.raises(NegativeValueError):
        require_non_negative(n)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, "Result: 5.0"),
        (10, 0, "Cannot divide by zero!"),
        (9, 3, "Result: 3.0"),
        (1, 0, "Cannot divide by zero!"),
        (-10, 2, "Result: -5.0"),
        (0, 5, "Result: 0.0"),
        (7, 7, "Result: 1.0"),
        (5, 0, "Cannot divide by zero!"),
        (100, 4, "Result: 25.0"),
        (3, 0, "Cannot divide by zero!"),
    ],
)
def test_divide_with_report(a, b, expected):
    assert divide_with_report(a, b) == expected


@pytest.mark.parametrize("age, expected", [(25, 25), (0, 0), (150, 150), (75, 75), (1, 1), (149, 149)])
def test_validate_age_valid(age, expected):
    assert validate_age(age) == expected


@pytest.mark.parametrize("age", [-1, 151, 200, -10])
def test_validate_age_raises(age):
    with pytest.raises(AssertionError):
        validate_age(age)


def _make_flaky(fail_count):
    calls = []

    def flaky():
        calls.append(1)
        if len(calls) <= fail_count:
            raise ValueError("not yet")
        return "ok"

    return flaky, calls


@pytest.mark.parametrize(
    "fail_count, attempts, should_raise, expected_calls",
    [
        (0, 3, False, 1),
        (1, 3, False, 2),
        (2, 3, False, 3),
        (3, 3, True, 3),
        (0, 1, False, 1),
        (1, 1, True, 1),
        (4, 5, False, 5),
        (5, 5, True, 5),
        (2, 2, True, 2),
        (0, 5, False, 1),
    ],
)
def test_retry(fail_count, attempts, should_raise, expected_calls):
    flaky, calls = _make_flaky(fail_count)
    if should_raise:
        with pytest.raises(ValueError):
            retry(flaky, attempts=attempts)
    else:
        assert retry(flaky, attempts=attempts) == "ok"
    assert len(calls) == expected_calls


@pytest.mark.parametrize(
    "password, expected_error",
    [
        ("Short1", "at least 8 characters"),
        ("longenough", "at least one digit"),
        ("lowercaseonly1", "at least one uppercase"),
        ("NoDigitsHere", "at least one digit"),
        ("short", "at least 8 characters"),
    ],
)
def test_validate_password_invalid(password, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        validate_password(password)


@pytest.mark.parametrize(
    "password",
    ["Valid1Password", "1234567A", "ALLUPPER1", "Aa1aaaaa", "Valid123Pass"],
)
def test_validate_password_valid(password):
    assert validate_password(password) == password
