"""Exercises: Control Flow (if/elif/else, match-case)."""


def classify_number(n: float) -> str:
    """Return "positive", "negative" or "zero" depending on n.
    Use if/elif/else.

    >>> classify_number(5)
    'positive'
    >>> classify_number(-5)
    'negative'
    >>> classify_number(0)
    'zero'
    """
    raise NotImplementedError("TODO: implement classify_number")


def grade_from_score(score: int) -> str:
    """Return a letter grade for score (0-100), using if/elif/else:
      90 <= score          -> "A"
      80 <= score < 90      -> "B"
      70 <= score < 80      -> "C"
      60 <= score < 70      -> "D"
      score < 60            -> "F"

    >>> grade_from_score(95)
    'A'
    >>> grade_from_score(61)
    'D'
    >>> grade_from_score(40)
    'F'
    """
    raise NotImplementedError("TODO: implement grade_from_score")


def describe_day(day: str) -> str:
    """Use a match-case statement (not if/elif) to return:
      "Weekend!" for "Saturday" or "Sunday"
      "Weekday" for anything else

    >>> describe_day("Saturday")
    'Weekend!'
    >>> describe_day("Monday")
    'Weekday'
    """
    raise NotImplementedError("TODO: implement describe_day")


def bmi_category(weight_kg: float, height_m: float) -> str:
    """Compute the Body Mass Index (weight_kg / height_m ** 2) and
    classify it:
      bmi < 18.5           -> "underweight"
      18.5 <= bmi < 25      -> "normal"
      25 <= bmi < 30        -> "overweight"
      bmi >= 30             -> "obese"

    >>> bmi_category(70, 1.75)
    'normal'
    """
    raise NotImplementedError("TODO: implement bmi_category")


def fizzbuzz(n: int) -> str:
    """Classic FizzBuzz: return "FizzBuzz" if n is divisible by both 3
    and 5, "Fizz" if only by 3, "Buzz" if only by 5, otherwise str(n).

    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(7)
    '7'
    """
    raise NotImplementedError("TODO: implement fizzbuzz")
