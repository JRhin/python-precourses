"""Exercises: Classes (attributes, magic methods, inheritance)."""


class Rectangle:
    """A rectangle with a width and a height.

    >>> r = Rectangle(3, 4)
    >>> r.area()
    12
    >>> r.perimeter()
    14
    >>> str(r)
    'Rectangle(3x4)'
    """

    def __init__(self, width: float, height: float):
        raise NotImplementedError("TODO: implement Rectangle.__init__")

    def area(self) -> float:
        raise NotImplementedError("TODO: implement Rectangle.area")

    def perimeter(self) -> float:
        raise NotImplementedError("TODO: implement Rectangle.perimeter")

    def __str__(self) -> str:
        raise NotImplementedError("TODO: implement Rectangle.__str__")


class Animal:
    """Base class for animals.

    >>> a = Animal("Generic Animal")
    >>> a.speak()
    '...'
    """

    def __init__(self, name: str):
        raise NotImplementedError("TODO: implement Animal.__init__")

    def speak(self) -> str:
        """Base implementation: animals don't say anything specific."""
        return "..."


class Dog(Animal):
    """A Dog is an Animal that barks.

    >>> d = Dog("Rex")
    >>> d.speak()
    'Rex says Woof!'
    """

    def speak(self) -> str:
        raise NotImplementedError("TODO: implement Dog.speak")


class Stack:
    """A last-in-first-out stack, backed internally by a list.

    >>> s = Stack()
    >>> s.is_empty()
    True
    >>> s.push(1)
    >>> s.push(2)
    >>> s.peek()
    2
    >>> s.pop()
    2
    >>> len(s)
    1
    """

    def __init__(self):
        raise NotImplementedError("TODO: implement Stack.__init__")

    def push(self, item) -> None:
        """Add item to the top of the stack."""
        raise NotImplementedError("TODO: implement Stack.push")

    def pop(self):
        """Remove and return the top item. Raise IndexError if empty."""
        raise NotImplementedError("TODO: implement Stack.pop")

    def peek(self):
        """Return (without removing) the top item. Raise IndexError if empty."""
        raise NotImplementedError("TODO: implement Stack.peek")

    def is_empty(self) -> bool:
        """Return True if the stack has no items."""
        raise NotImplementedError("TODO: implement Stack.is_empty")

    def __len__(self) -> int:
        raise NotImplementedError("TODO: implement Stack.__len__")


class BankAccount:
    """A simple bank account that tracks a balance and rejects invalid
    operations by raising ValueError.

    >>> acc = BankAccount(100)
    >>> acc.deposit(50)
    >>> acc.balance
    150
    >>> acc.withdraw(30)
    >>> acc.balance
    120
    """

    def __init__(self, balance: float = 0):
        """Store the starting balance. Raise ValueError if balance < 0."""
        raise NotImplementedError("TODO: implement BankAccount.__init__")

    def deposit(self, amount: float) -> None:
        """Add amount to the balance. Raise ValueError if amount <= 0."""
        raise NotImplementedError("TODO: implement BankAccount.deposit")

    def withdraw(self, amount: float) -> None:
        """Subtract amount from the balance. Raise ValueError if amount <= 0
        or if amount is greater than the current balance."""
        raise NotImplementedError("TODO: implement BankAccount.withdraw")
