import pytest

from src.classes import Animal, BankAccount, Dog, Rectangle, Stack


@pytest.mark.parametrize(
    "width, height, area, perimeter, string",
    [
        (3, 4, 12, 14, "Rectangle(3x4)"),
        (1, 1, 1, 4, "Rectangle(1x1)"),
        (5, 2, 10, 14, "Rectangle(5x2)"),
        (10, 10, 100, 40, "Rectangle(10x10)"),
        (0, 5, 0, 10, "Rectangle(0x5)"),
        (7, 3, 21, 20, "Rectangle(7x3)"),
        (2.5, 4, 10.0, 13.0, "Rectangle(2.5x4)"),
        (6, 6, 36, 24, "Rectangle(6x6)"),
        (100, 1, 100, 202, "Rectangle(100x1)"),
        (8, 5, 40, 26, "Rectangle(8x5)"),
    ],
)
def test_rectangle(width, height, area, perimeter, string):
    r = Rectangle(width, height)
    assert r.area() == area
    assert r.perimeter() == perimeter
    assert str(r) == string


@pytest.mark.parametrize(
    "name",
    ["Rex", "Fido", "Buddy", "Max", "Bella", "Charlie", "Luna", "Rocky", "Daisy", "Zeus"],
)
def test_dog_speak(name):
    assert Dog(name).speak() == f"{name} says Woof!"


def test_animal_base_speak_is_generic():
    assert Animal("Generic Animal").speak() == "..."


def test_dog_is_an_animal():
    d = Dog("Rex")
    assert isinstance(d, Animal)


def test_stack_push_and_pop_lifo_order():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def test_stack_is_empty():
    s = Stack()
    assert s.is_empty() is True
    s.push("x")
    assert s.is_empty() is False


def test_stack_len():
    s = Stack()
    assert len(s) == 0
    s.push(1)
    s.push(2)
    assert len(s) == 2
    s.pop()
    assert len(s) == 1


def test_stack_peek_does_not_remove():
    s = Stack()
    s.push(42)
    assert s.peek() == 42
    assert s.peek() == 42
    assert len(s) == 1


def test_stack_pop_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_stack_peek_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()


def test_stack_mixed_types():
    s = Stack()
    s.push(1)
    s.push("two")
    s.push([3])
    assert s.pop() == [3]
    assert s.pop() == "two"
    assert s.pop() == 1


@pytest.mark.parametrize(
    "initial, ops, expected",
    [
        (100, [("deposit", 50)], 150),
        (100, [("withdraw", 30)], 70),
        (0, [("deposit", 10), ("withdraw", 5)], 5),
        (50, [("withdraw", 50)], 0),
        (100, [("withdraw", 150)], "ValueError"),
        (100, [("deposit", -10)], "ValueError"),
        (100, [("withdraw", -10)], "ValueError"),
        (-10, [], "ValueError"),
        (200, [("deposit", 100), ("withdraw", 50), ("deposit", 25)], 275),
        (0, [("withdraw", 1)], "ValueError"),
    ],
)
def test_bank_account(initial, ops, expected):
    if expected == "ValueError":
        with pytest.raises(ValueError):
            acc = BankAccount(initial)
            for kind, amount in ops:
                getattr(acc, kind)(amount)
    else:
        acc = BankAccount(initial)
        for kind, amount in ops:
            getattr(acc, kind)(amount)
        assert acc.balance == expected
