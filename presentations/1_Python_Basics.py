# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.24.0",
#     "torch==2.14.0",
#     "transformers==5.16.1",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(layout_file="layouts/1_Python_Basics.slides.json")


@app.cell(hide_code=True)
def setup_helpers():
    import marimo as mo
    import pydoc as _pydoc
    import timeit as _timeit_module
    import statistics as _statistics

    def print(*args, sep=' ', end='\n'):
        mo.output.append(sep.join(str(a) for a in args) if args else '')

    def help(obj):
        mo.output.append(mo.plain_text(_pydoc.plain(_pydoc.render_doc(obj, title='Help on %s'))))

    def input(prompt='', value=''):
        return mo.ui.text(value=value, label=prompt)

    def _fmt_time(x):
        for scale, unit in ((1, 's'), (1e-3, 'ms'), (1e-6, '\u00b5s'), (1e-9, 'ns')):
            if x >= scale:
                return f'{x / scale:.3g} {unit}'
        return f'{x * 1e9:.3g} ns'

    def timeit(stmt, repeat=7):
        """marimo-friendly stand-in for IPython's %timeit magic."""
        timer = _timeit_module.Timer(stmt)
        number, _ = timer.autorange()
        times = [t / number for t in timer.repeat(repeat=repeat, number=number)]
        mean = _statistics.mean(times)
        stdev = _statistics.stdev(times) if len(times) > 1 else 0.0
        print(f'{_fmt_time(mean)} \u00b1 {_fmt_time(stdev)} per loop '
              f'(mean \u00b1 std. dev. of {repeat} runs, {number} loops each)')

    return help, input, mo, print, timeit


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 🐍 Pythoneer **Crash** Course
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🥜 Python in a nutshell
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="display:flex;justify-content:center;align-items:center;gap:16px;">
      <img src="https://exyte.com/upload/guido-headshot-2019.jpg" width="600">
      <img src="https://images3.alphacoders.com/157/157.jpg" width="750">
    </div>

    *  **High-level**, **interpreted language** known for **readability** and **simplicity**.
    *  **Uses indentation** instead of curly braces to define code blocks.
    *  Versatile: powers web apps, data science, AI, automation, and more.
    *  Created by **Guido van Rossum** in 1991.
    *  Named after **Monty Python**, not the snake!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🐍 Why Python?

    <div style="display:flex;align-items:center;gap:24px;">
      <div style="flex:0 0 auto;text-align:center;">
        <img src="https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qdom9lf3g0y60rhv90um.jpg" height="200">
      </div>
      <div style="flex:1;">
        Because...
        <ul>
          <li>It looks like English</li>
          <li>It runs <b>almost everywhere</b></li>
          <li>It has a package for literally <b>everything</b> (<a href="https://scipy.org/">SciPy</a>, <a href="https://scikit-learn.org/stable/index.html">scikit-learn</a>, <a href="https://pypi.org/project/cowsay/">cowsay</a> and more...)</li>
          <li>It makes <b>you feel smarter than you are</b></li>
        </ul>
      </div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    > *“Python is executable pseudocode.”* – Guido van Rossum
    """)
    return


@app.cell
def _(mo):
    with mo.redirect_stdout():
        import this
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Easter egg**:

    1. Open a terminal.
    2. Run `python`.
    3. Then simply type `import antigravity`.
    4. enjoy...
    """)
    return


@app.cell
def _(print):
    from transformers import pipeline

    classifier = pipeline("sentiment-analysis")
    print(classifier("Python is amazing!"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Reference**: [transformers package](https://pypi.org/project/transformers/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 👋 Hello, World!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="display:flex;justify-content:center;align-items:center;gap:16px;">
      <img src="https://i.imgflip.com/99tv22.jpg" height="320">
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    <div style="display:flex;justify-content:center;align-items:center;gap:16px;">
      <img src="https://i.programmerhumor.io/2022/11/programmerhumor-io-python-memes-backend-memes-2391d88151750ff.jpg" height="220">
    </div>
    """)
    return


@app.cell
def _(print):
    print("Hello, World!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    How it Works:

    *   `print()` → a built-in function that displays output.
    *   `"Hello, World!"` → a string (text inside quotes).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 💭 Comments
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Everything after `#` on that line is ignored by Python, so it’s only for humans reading the code.
    """)
    return


@app.cell
def _(print):
    # This is a comment. Python will ignore it.
    x = 10  # Comments can also go at the end of a line of code

    print(x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    👉 Use `#` whenever you want to explain what your code does, make notes, or temporarily disable code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ⚠️⚠️⚠️ **Proceed with Caution!!!** ⚠️⚠️⚠️
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In Python, you *can* use standalone strings (string literals not assigned to a variable) as a form of comment, but **this is highly discouraged**.
    """)
    return


@app.cell
def _(print):
    "Define an important variable named pippo"
    pippo = 10

    print("Say hello to pippo! Its value is:", pippo)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In Python, a string literal by itself is a valid statement. If it’s not assigned to a variable or used, it simply gets created and then immediately discarded. For example:
    """)
    return


@app.cell
def _():
    "This looks like a comment, but it's actually a string literal."
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python will parse it, allocate it, and then throw it away at runtime (unless it’s the first statement in a module, class, or function, in which case it becomes a **docstring**).

    Why is **discouraged**:

    1.   It **confuses readers** — people might think it’s a docstring or code that does something.
    2.   It **wastes resources** — even though small, Python still creates the string object before discarding it.
    3.   It **isn’t the standard** — PEP 8 ([Python Styling Bible](https://peps.python.org/pep-0008/)) explicitly recommends using `#` for comments.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The correct way to write comments is with the `#` symbol for single-line comments.
    """)
    return


@app.cell
def _(print):
    # This is the right way to write a comment.

    print('Got it?')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or docstrings (`\"\"\" ... \"\"\"`), for documenting modules, classes, and functions:
    """)
    return


@app.cell
def _(help):
    def add(a, b):
            """Return the sum of a and b."""
            return a + b

    help(add)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 📦 Python Variables & Types
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A **variable** is like a **labeled box** in your program where you can store a value (number, text, or more).

    *   You can look inside the box, change its contents, and use it anywhere in your program (more later).
    """)
    return


@app.cell
def _(print):
    # Define a variable and assign it an initial value
    x_1 = 4
    print('Initial value:', x_1)

    # Update the variable with a new value
    x_1 = 10
    print('Changed value:', x_1)
    return (x_1,)


@app.cell
def _(print, x_1):
    # Access the variable again to retrieve its current value
    print(x_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see an example:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | Variable       | Value       | Data Type | Description                               |
    |----------------|------------|-----------|-------------------------------------------|
    | age            | 25         | int       | Represents a whole number (e.g., age in years) |
    | user_name      | "Pippo"    | str       | Text string representing a name          |
    | height_in_m    | 1.75       | float     | Decimal number representing height in meters |
    | is_student     | True       | bool      | Boolean value indicating student status  |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In Python:
    """)
    return


@app.cell
def _(print):
    age = 25
    user_name = "Pippo"
    height_in_m = 1.75
    is_student = True

    print(age, user_name, height_in_m, is_student)
    return age, height_in_m, is_student, user_name


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In Python, you don’t need to declare the type of a variable; it’s inferred automatically.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Equivalent C Variable Declarations:

    ```c
    #include <stdio.h>
    #include <stdbool.h>  // for bool type in C99

    int main() {
        int age = 25;                  // integer
        char user_name[] = "Pippo";    // string (array of chars)
        float height_in_m = 1.75;      // floating-point number
        bool is_student = true;        // boolean (true/false in C99)

        // Example of printing values
        printf("Age: %d\n", age);
        printf("Name: %s\n", user_name);
        printf("Height: %.2f\n", height_in_m);
        printf("Is student: %d\n", is_student);

        return 0;
    }
    ```

    **Key Differences from Python:**

    *    You must declare the type of every variable (`int`, `float`, `char[]`, `bool`).
    *    Strings are arrays of characters in C, not a built-in type.
    *    Booleans require `#include <stdbool.h>` (in C99 or later).
    *    The type **cannot change** after declaration.
    *    Python statements do not end with semicolons (`;`).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The `type()` function:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `type()` function returns the data type of a variable or value.
    """)
    return


@app.cell
def _(age, height_in_m, is_student, print, user_name):
    print('Type of age:', type(age))
    print('Type of user_name:', type(user_name))
    print('Type of height_in_m:', type(height_in_m))
    print('Type of is_student:', type(is_student))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Works with **expressions** too:
    """)
    return


@app.cell
def _(print):
    print(type(10 + 3.5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **PEP 8 Tips**:

    *   Use lowercase with underscores for variables
    *   Be descriptive: `user_name` > `n`
    *   (Optional) Add type hints: `age: int = 25`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ⚠️⚠️⚠️ **Proceed with Caution!!!** ⚠️⚠️⚠️
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Type Hints are just hints!
    """)
    return


@app.cell
def _(print):
    x_2: int = 10
    print('Before:', type(x_2))
    x_2: int = "it's never to late to change."
    print('After:', type(x_2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🔢 Numeric Operators
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Integers
    """)
    return


@app.cell
def _(print):
    a, b = 11, 5

    print('a + b = ', a + b)   # addition
    print('a - b = ', a - b)   # subtraction
    print('a / b = ', a / b)   # float division
    print('a // b = ', a // b) # integer (floor) division
    print('a % b = ', a % b)   # modulo (remainder of division)
    print('a * b = ', a * b)   # multiplication
    print('a ** b = ', a ** b) # exponentiation (a to the power of b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Float
    """)
    return


@app.cell
def _(print):
    a_1, b_1 = (2.1, 2.3)
    print('a + b = ', a_1 + b_1)
    print('a - b = ', a_1 - b_1)  # addition
    print('a / b = ', a_1 / b_1)  # subtraction
    print('a // b = ', a_1 // b_1)  # float division
    print('a % b = ', a_1 % b_1)  # integer (floor) division
    print('a * b = ', a_1 * b_1)  # modulo (remainder of division)
    print('a ** b = ', a_1 ** b_1)  # multiplication  # exponentiation (a to the power of b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Mixed
    """)
    return


@app.cell
def _(print):
    a_2, b_2 = (2, 3.14)
    print('a + b = ', a_2 + b_2)
    print('a - b = ', a_2 - b_2)  # addition
    print('a / b = ', a_2 / b_2)  # subtraction
    print('a // b = ', a_2 // b_2)  # float division
    print('a % b = ', a_2 % b_2)  # integer (floor) division
    print('a * b = ', a_2 * b_2)  # modulo (remainder of division)
    print('a ** b = ', a_2 ** b_2)  # multiplication  # exponentiation (a to the power of b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Augmented Assignment Operators
    """)
    return


@app.cell
def _(print):
    x_3 = 10
    print('Starting value for x =', x_3)
    x_3 = x_3 + 5
    print('x += 5 --> x = x + 5 =', x_3)
    # +=  (Add and assign)
    x_3 = x_3 - 3  # x = x + 5
    print('x -= 3 --> x = x - 3 =', x_3)  # 15
    x_3 = x_3 * 2
    # -=  (Subtract and assign)
    print('x *= 2 --> x = x * 2 =', x_3)  # x = x - 3
    x_3 = x_3 / 4  # 12
    print('x /= 4 --> x = x / 4 =', x_3)
    # *=  (Multiply and assign)
    x_3 = x_3 // 2  # x = x * 2
    print('x //= 2 --> x = x // 2 =', x_3)  # 24
    x_3 = x_3 % 2
    # /=  (Divide and assign)
    print('x %= 2 --> x = x % 2 =', x_3)  # x = x / 4
    x_3 = x_3 ** 3  # 6.0
    # //=  (Floor divide and assign)
    # %=  (Modulus and assign)
    # **=  (Exponent and assign)
    print('x **= 3 --> x = x ** 3 =', x_3)  # x = x // 2  # 3.0  # x = x % 2  # 1.0  # x = x ** 3  # 1.0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🖯 Boolean Operators 101
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `==` and `!=` operators
    """)
    return


@app.cell
def _(print):
    x_4 = 10
    print('x == 10  -->', x_4 == 10)
    print('x != 10  -->', x_4 != 10)  # True: checks if x is equal to 10; note that = is for assignment, == is for comparison
    print('x != 5   -->', x_4 != 5)  # False: checks if x is not equal to 10
    print('x == 5   -->', x_4 == 5)  # True: checks if x is not equal to 5  # False: checks if x is equal to 5
    return (x_4,)


@app.cell
def _(print, x_4):
    # The comparison also works between integers and floats
    print('x == 10.0  -->', x_4 == 10.0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `<`, `>`, `<=` and `>=` operators
    """)
    return


@app.cell
def _(print, x_4):
    print('x < 10   -->', x_4 < 10)  # False, because 10 is not less than 10
    print('x > 3    -->', x_4 > 3)  # True, because 10 is greater than 3
    print('x <= 10  -->', x_4 <= 10)  # True, because 10 is equal to 10
    print('x >= 5   -->', x_4 >= 5)  # True, because 10 is greater than 5
    print('5 < x < 11   -->', 5 < x_4 < 11)
    # Chained comparisons
    print('0 <= x <= 10  -->', 0 <= x_4 <= 10)  # True, because 5 < 10 < 11  # True, because 0 <= 10 <= 10
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `and` operator
    """)
    return


@app.cell
def _(print):
    print('True and True: ', True and True)    # True: both operands are True, so the result is True
    print('True and False: ', True and False)  # False: one operand is False, so the result is False
    print('False and False: ', False and False) # False: both operands are False, so the result is False
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `or` operator
    """)
    return


@app.cell
def _(print):
    print('True or True: ', True or True)      # True: at least one operand is True, so the result is True
    print('True or False: ', True or False)    # True: at least one operand is True, so the result is True
    print('False or False: ', False or False)  # False: both operands are False, so the result is False
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `is` and `not` operators
    """)
    return


@app.cell
def _(print):
    print('True is True: ', True is True)           # True: checks if the object on the left is the same as the object on the right
    print('True is not False: ', True is not False) # True: checks if the objects are not the same
    print('not False: ', not False)                 # True: inverts the boolean value; not False becomes True
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Combining operators
    """)
    return


@app.cell
def _(print):
    print('3 < 4 and 4 == 4  -->', 3 < 4 and 4 == 4)
    # True: both comparisons are True, so 'and' returns True

    print('3 == 4 or 4 == 4  -->', 3 == 4 or 4 == 4)
    # True: first comparison is False, second is True, 'or' returns True because at least one operand is True

    print('3 == 4 or not (4 == 0)  -->', 3 == 4 or not (4 == 0))
    # True: 3 == 4 is False, but 4 == 0 is False, so 'not (4 == 0)' is True; 'or' returns True
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Note**:

    In Python, booleans (`True` and `False`) are subtypes of integers, where `True` behaves like `1` and `False` behaves like `0`.
    """)
    return


@app.cell
def _(print):
    print(True == 1)   # True: in Python, True is equivalent to 1 when compared with ==
    print(False == 0)  # True: in Python, False is equivalent to 0 when compared with ==
    return


@app.cell
def _(print):
    print("True and 1:", True and 1)    # 1: 'and' returns the second value if the first is True
    print("True or 1:", True or 1)      # True: 'or' returns the first value if it is True
    print("False and 1:", False and 1)  # False: 'and' returns the first value if it is False
    print("False or 1:", False or 1)    # 1: 'or' returns the second value if the first is False

    print('True and 0:', True and 0)    # 0: 'and' returns the second value if the first is True
    print('True or 0:', True or 0)      # True: 'or' returns the first value if it is True
    print('False and 0:', False and 0)  # False: 'and' returns the first value if it is False
    print('False or 0:', False or 0)    # 0: 'or' returns the second value if the first is False
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What happens if I use `and` or `or` to compare a variable, such as a string, with a boolean value in Python?
    """)
    return


@app.cell
def _(print):
    x_5 = 'something'  # You can also try x = "", x = None, or x = "something"
    print('x and True:', x_5 and True)

    print('False and x:', False and x_5)  # True if x is truthy (non-empty string), else returns x itself (falsy)
    print('True or x:', True or x_5)  # Always False: 'and' returns the first falsy value
    print('x or False:', x_5 or False)  # Always True: 'or' returns the first truthy value  # Returns x if x is truthy, else False
    return (x_5,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What happens if I change the order between the values?
    """)
    return


@app.cell
def _(print, x_5):
    print('Using and:', (x_5 and True) == (True and x_5))
    # False in most cases: 'and' is **not commutative**; it returns the first falsy value or the last value if all are truthy
    # False in most cases: 'or' is also **not commutative**; it returns the first truthy value or the last value if all are falsy
    print('Using or:', (True or x_5) == (x_5 or True))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ⚠️⚠️⚠️ **Proceed with Caution!!!** ⚠️⚠️⚠️
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In Python (and most programming languages), using `==` with floating-point numbers can lead to approximation errors because floating-point numbers can’t always represent decimal values exactly.

    Here's a classic example:
    """)
    return


@app.cell
def _(print):
    a_3 = 0.1 + 0.2
    b_3 = 0.3
    print(a_3 == b_3)
    print('a =', a_3)  # False: floating-point arithmetic can introduce tiny approximation errors
    print('b =', b_3)  # 0.30000000000000004, not exactly 0.3  # 0.3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One way to handle this is by using a tolerance with `math.isclose()` (see the [documentation](https://docs.python.org/3/library/math.html#math.isclose) for more).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 📃 Strings
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A string is a **sequence of characters** that represents text in your program.

    *   Think of it as a chain of letters, numbers, or symbols enclosed in quotes.
    *   Strings can include words, sentences, numbers (as text), or any combination of characters.
    """)
    return


@app.cell
def _():
    "This is a string."
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Strings are enclosed in single ' ' or double " " quotes.

    **Note**:

    Use double quotes `" "` when your string contains a single quote `'` to avoid syntax errors, or escape the single quote with a backslash `\`.
    """)
    return


app._unparsable_cell(
    r"""
    'it's never to late to change.'
    """,
    name="_"
)


@app.cell
def _():
    "it's never to late to change."
    return


@app.cell
def _():
    'it\'s never to late to change.'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key Takeaway**:

    > Single vs double quotes are interchangeable in Python, but choose the one that avoids conflicts with quotes inside your string.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Operators with Strings
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `+` and `*` operators
    """)
    return


@app.cell
def _(print):
    print('Hello, ' + 'World!') # String concatenation: combines two strings into one
    print('Hello' * 3) # String repetition: repeats the string 3 times
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### String Functions
    """)
    return


@app.cell
def _(print):
    x_6 = "I'm a beautiful string"
    print('len(x) -->', len(x_6))
    print('x.startswith("ok") -->', x_6.startswith('ok'))  # Returns the length of the string
    print('x.endswith("ing") -->', x_6.endswith('ing'))  # Checks if the string starts with "ok"
    print('x.find("string") -->', x_6.find('string'))  # Checks if the string ends with "ing"
    print('x.islower() -->', x_6.islower())  # Returns the starting index of the substring "string"
    print('x.replace("beautiful", "bad") -->', x_6.replace('beautiful', 'bad'))  # Checks if all characters are lowercase
    print('x.split() -->', x_6.split())  # Replaces a substring
    words = x_6.split()
    # Splitting the string into a list of words
    # Joining a list of words back into a string
    print('" ".join(words) -->', ' '.join(words))  # ['I\'m', 'a', 'beautiful', 'string']  # "I'm a beautiful string"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### String Slicing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    String slicing is a way to extract a portion (substring) of a string by specifying a start index, an end index, and an optional step. The syntax is:

    ```python
    'some string'[start:end:step]
    ```

    *   `start` – the index to begin the slice (inclusive; defaults to 0 if omitted)
    *   `end` – the index to end the slice (exclusive; defaults to the end of the string if omitted)
    *   `step` – how many characters to skip (optional; defaults to 1; can be negative to reverse)

    It allows you to retrieve, skip, or reverse parts of a string efficiently without modifying the original string.
    """)
    return


@app.cell
def _(print):
    s = "Hello, World!"

    print(s)
    print()

    # Basic slicing: s[start:end] -> from index start up to (but not including) end
    print('s[0:5] -->', s[0:5])       # 'Hello': characters from index 0 to 4

    # Omitting start (defaults to 0)
    print('s[:5] -->', s[:5])         # 'Hello': same as s[0:5]

    # Omitting end (goes to the end of the string)
    print('s[7:] -->', s[7:])         # 'World!': from index 7 to the end

    # Negative indices count from the end
    print('s[-6:-1] -->', s[-6:-1])   # 'World': starts 6 from the end up to 1 from the end

    # Using step: s[start:end:step]
    print('s[::2] -->', s[::2])       # 'Hlo ol!': every 2nd character

    # Reverse a string using slicing
    print('s[::-1] -->', s[::-1])     # '!dlroW ,olleH': reverses the string

    # Extracting a single character
    print('s[1] -->', s[1])           # 'e': character at index 1

    # Negative step with slicing
    print('s[10:5:-1] -->', s[10:5:-1]) # 'rloW': slice backwards from index 10 to 6
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *   `start` is inclusive, `end` is exclusive.
    *   You can omit start or end to go from the beginning or to the end.
    *   `step` lets you skip characters or reverse the string.
    *   Negative indices and negative steps allow counting or slicing from the end.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Formatting Strings
    """)
    return


@app.cell
def _(print):
    pi = 3.14159
    radius = 5
    area = pi * radius ** 2

    print('The radius and the area of the circle are:', radius, area)
    return area, pi, radius


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### f-Strings (Python 3.6+) [Suggested]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Start the string with `f` and use `{}` to insert variables.
    """)
    return


@app.cell
def _(area, print, radius):
    print(f"The area of a circle with radius {radius} is {area}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Supports expressions directly:
    """)
    return


@app.cell
def _(pi, print, radius):
    print(f"The area of a circle with radius {radius} is {pi * radius ** 2}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Applying decimal approximations:
    """)
    return


@app.cell
def _(area, print, radius):
    print(f"The area of a circle with radius {radius} is {area:.2f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With “self-documenting expressions”:
    """)
    return


@app.cell
def _(area, print, radius):
    print(f'A circle with {radius=} has {area=:.2f}.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And [more](https://www.youtube.com/watch?v=EoNOWVYKyo0)...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Using `.format()` [Old Method]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use `{}` as placeholders and call `.format()` on the string.
    """)
    return


@app.cell
def _(area, print, radius):
    print("The area of a circle with radius {} is {}".format(radius, area))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Can also use named placeholders:
    """)
    return


@app.cell
def _(area, print, radius):
    print("The area of a circle with radius {r} is {a}".format(r=radius, a=area))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Applying decimal approximations:
    """)
    return


@app.cell
def _(area, print, radius):
    print("The area of a circle with radius {} is {:.2f}".format(radius, area))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🪄 Casting
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Casting** is the process of *converting a value from one data type to another*.

    *   Also called **type conversion**.
    *   Useful when a value’s type does not match the operation you want to perform.
    """)
    return


@app.cell
def _(print):
    # Convert value to integer
    num_str = "25"
    num_int = int(num_str)  # converts string to integer
    print(num_int, type(num_int))

    # Convert value to float
    pi_str = "3.14"
    pi_float = float(pi_str)  # converts string to float
    print(pi_float, type(pi_float))

    # Convert value to string
    num = 10
    num_str2 = str(num)  # converts integer to string
    print(num_str2, type(num_str2))

    # Convert value to boolean
    val = 0
    val_bool = bool(val)  # converts 0 to False, non-zero numbers to True
    print(val_bool, type(val_bool))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Why Casting is Needed:

    *   `input()` always returns a string, even for numbers
    *   To perform arithmetic or logical operations, you often need to convert the string to a number
    """)
    return


@app.cell
def _(input):
    age_input = input('Enter your age:', '25')
    age_input
    return (age_input,)


@app.cell(hide_code=True)
def _(age_input, print):
    age_1 = age_input.value # Usually, .value is not needed, but it is required here when using marimo 
    print('Before casting:', type(age_1))  # <class 'str'>
    age_1 = int(age_1)
    # Convert to integer
    print('After casting:', type(age_1))  # <class 'int'>
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 📋 Lists
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is a List?

    *   A list is an **ordered, mutable collection of items**.
    *   Can store different data types in one list.
    *   Can store duplicates.
    *   Defined using square brackets `[ ]`.
    """)
    return


@app.cell
def _(print):
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "Pippo", 3.14, True, ['Nested', 'Lists']]

    print(fruits)
    print(numbers)
    print(mixed)
    return (fruits,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Accessing List Elements
    """)
    return


@app.cell
def _(fruits, print):
    print(fruits[0])   # apple  (first element)
    print(fruits[-1])  # cherry (last element)
    print(fruits[0:2]) # ['apple', 'banana'] (slicing)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Modifying Lists
    """)
    return


@app.cell
def _(print):
    fruits_1 = ['apple', 'banana', 'banana', 'cherry']
    print('Initial state -->', fruits_1)
    print()
    fruits_1.append('orange')
    # Add items
    print('Add item to the bottom -->', fruits_1)
    print()
    fruits_1.insert(1, 'pear')
    print('Insert at position 1 -->', fruits_1)
    print()  # insert at position 1
    fruits_1.remove('banana')
    print('Remove first istance of item (from left) -->', fruits_1)
    print()
    # Remove items
    last_item = fruits_1.pop()
    print('Remove last item -->', fruits_1)
    print(f'last_item={last_item!r}')
    print()  # removes last element
    fruits_1[0] = 'strawberry'
    print('Change item at position 0 -->', fruits_1)
    # Change item
    print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Other List Functions
    """)
    return


@app.cell
def _(print):
    numbers_1 = [3, 1, 4, 1, 5, 9]
    print('Length:', len(numbers_1))
    print('Item summation:', sum(numbers_1))  # number of elements in the list
    print('Get the minimum value:', min(numbers_1))  # sum of all elements
    print('Get the largest value:', max(numbers_1))  # smallest element
    numbers_1.sort()  # largest element
    print('Ascending order:', numbers_1)
    # Sort the list in ascending order (default)
    numbers_1.sort(reverse=True)
    # Sort the list in descending order
    print('Descending order:', numbers_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### `+` operator
    """)
    return


@app.cell
def _(print):
    fruits_2 = ['apple', 'banana']
    vegetables = ['carrot', 'potato']

    # Join two lists together
    food = fruits_2 + vegetables

    print('Concatenated list:', food)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### `*` operators
    """)
    return


@app.cell
def _(print):
    numbers_2 = [1, 2, 3]
    repeated = numbers_2 * 6

    # Repeat the list 6 times
    print('Repeated list:', repeated)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    [Pop Reference](https://www.youtube.com/watch?v=2vjPBrBU-TM&list=RD2vjPBrBU-TM&start_radio=1&t=31s)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧺 Sets
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is a Set?

    *   A set is **an unordered collection of unique elements**.
    *   Defined using curly braces `{}` or the `set()` function.
    """)
    return


@app.cell
def _(print):
    numbers_3 = {1, 2, 3, 3, 4, 4}
    print(numbers_3)  # {1, 2, 3, 4} → duplicates removed
    fruits_3 = set(['apple', 'banana', 'apple'])
    print(fruits_3)
    mixed_set = {1, 'apple', 3.14, True}  # {'apple', 'banana'}
    print(mixed_set)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *   All set elements **must be hashable** (immutable types)
    *   Cannot include lists or dictionaries as elements:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Adding & Removing Elements
    """)
    return


@app.cell
def _(print):
    numbers_4 = {1, 2, 3}
    numbers_4.add(4)
    # Add an element
    print(numbers_4)
    numbers_4.remove(2)  # {1, 2, 3, 4}
    print(numbers_4)
    # Remove an element
    # Remove an element safely (no error if missing)
    numbers_4.discard(10)  # {1, 3, 4}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Set Operations
    """)
    return


@app.cell
def _(print):
    a_4 = {1, 2, 3}
    b_4 = {3, 4, 5}
    print('Union -->', a_4 | b_4)
    # Union (all elements)
    print('Intersecation -->', a_4 & b_4)  # {1, 2, 3, 4, 5}
    print('Difference -->', a_4 - b_4)
    # Intersection (common elements)
    # Difference (elements in a but not b)
    # Symmetric Difference (elements in a or b, not both)
    print('Symmetric Difference -->', a_4 ^ b_4)  # {3}  # {1, 2}  # {1, 2, 4, 5}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Set Functions
    """)
    return


@app.cell
def _(print):
    numbers_5 = {3, 1, 4, 5, 9}
    print('Length:', len(numbers_5))
    print('Item summation:', sum(numbers_5))  # number of elements in the set
    print('Get the minimum value:', min(numbers_5))  # sum of all elements
    print('Get the largest value:', max(numbers_5))  # smallest element  # largest element
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Difference in "per-for-mAHns"
    """)
    return


@app.cell
def _(print, timeit):
    # Prepare test data
    N = 5_000_000
    numbers_list = list(range(N))
    numbers_set = set(range(N))

    target = N - 1  # element at the end (worst case scenario)

    # %timeit is a Jupyter magic command, not valid Python -- use our own timeit() instead
    print('List search:')
    timeit(lambda: target in numbers_list)

    print('Set search:')
    timeit(lambda: target in numbers_set)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Expected Results**

    *   List search → much slower, because Python must scan through elements one by one ($O(n)$).

    *   Set search → very fast, because sets use hash tables for lookups ($O(1)$ average).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Note**: `%timeit` is one of the IPython Magic function, which can be used to time a particular piece of code (see [this](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html#magic-functions) for more). Here we use a small custom timeit() helper instead that reproduces the same timing output.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🪨 Tuples
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is a Tuple?

    *   A tuple is **an ordered, immutable collection of items**.
    *   Defined using parentheses `( )`.
    *   Can contain mixed types (numbers, strings, booleans, etc.).
    """)
    return


@app.cell
def _(print):
    dimensions = (1920, 1080)
    person = ("Pippo", 25, True)

    print(dimensions)
    print(person)
    return (person,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Accessing Elements
    """)
    return


@app.cell
def _(person, print):
    print(person[0])    # Pippo (first element)
    print(person[-1])   # True (last element)
    print(person[0:2])  # ('Pippo', 25) (slicing)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Tuple Operations
    """)
    return


@app.cell
def _(print):
    numbers_6 = (1, 2, 3)
    letters = ('a', 'b')
    combined = numbers_6 + letters
    # Concatenation
    print(combined)
    repeated_1 = numbers_6 * 2  # (1, 2, 3, 'a', 'b')
    # Repetition
    print(repeated_1)  # (1, 2, 3, 1, 2, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Tuple Functions
    """)
    return


@app.cell
def _(print):
    numbers_7 = (3, 1, 4, 1, 5)
    print('Length:', len(numbers_7))
    print('Item summation:', sum(numbers_7))  # number of elements in the tuple
    print('Get the minimum value:', min(numbers_7))  # sum of all elements
    print('Get the largest value:', max(numbers_7))  # smallest element  # largest element
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Modifying Tuples
    """)
    return


@app.cell
def _(person):
    person[0] = 'Vercingetorix'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 📓 Dictionaries
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is a Dictionary?

    *   A dictionary is a collection of key–value pairs.
    *   Defined using curly braces `{}` with `key: value` syntax.
    """)
    return


@app.cell
def _(print):
    person_1 = {'name': 'Pippo', 'age': 25, 'height_in_m': 1.75, 'is_student': True}
    print(person_1)
    return (person_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Key Properties:

    *   Keys must be **unique and immutable** (e.g., strings, numbers, tuples)
    *   Values can be any type (string, int, list, dict, etc.)
    *   **Unordered** (insertion order is preserved from Python 3.7+)
    *   Mutable (you can add, change, or remove items)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Accessing Values
    """)
    return


@app.cell
def _(person_1, print):
    print('The person name is:', person_1['name'])  # Pippo
    print('The person age is:', person_1.get('age'))  # 25
    print('The person height in feet is:', person_1.get('height_in_feet', 'Not found'))  # safer access with default
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key Takeaway**

    *   Use `[]` when you are sure the key exists.
    *   Use `.get()` when the key may be missing and you want to avoid errors.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Modifying Dictionaries
    """)
    return


@app.cell
def _(person_1, print):
    # Add a new key–value pair
    person_1['city'] = 'Rome'
    print(person_1)
    print()
    person_1['age'] = 26
    # Change an existing value
    print(person_1)
    print()
    person_1.pop('is_student')
    del person_1['height_in_m']
    print(person_1)
    # Remove a key–value pair
    print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dictionaries Functions
    """)
    return


@app.cell
def _(person_1, print):
    print(person_1.keys())  # dict_keys(['name', 'age', 'city'])
    print(person_1.values())  # dict_values(['Pippo', 26, 'Rome'])
    print(person_1.items())  # dict_items([('name','Pippo'),('age',26),('city','Rome')])
    return


@app.cell
def _(person_1, print):
    person_1.clear()  # removes all items

    print(person_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🌊 Control Flow
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What Are Conditional Statements?

    *   Allow the program to make decisions based on conditions.

    *   Syntax: `if`, `elif`, `else`

    **Intuition**: “If this is true, do something; else, do something else.”
    """)
    return


@app.cell
def _(print):
    x_7 = 10
    if x_7 > 0:
        print('x is positive')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Only executes the indented block if the condition is **True**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Note**: Unlike C and many other programming languages, Python uses indentation to define code blocks. Instead of curly braces `{}` to indicate different levels of code, Python relies on **consistent spacing**.

    ```python
    # Pythonic way...
    if x > 0:
        print("x is positive")
    ```

    *   The **indentation** under the `if` statement defines the block of code that runs when the condition is true.
    *   No curly braces `{}` are needed.

    ```c
    // C style
    if (x > 0) {
        printf("x is positive\n");
    }
    ```

    *   The **curly braces** `{}` indicate which statements belong to the if block.
    *   Indentation is optional and only for readability.

    **Key Takeaways**:

    *   **Python**: Code structure is defined by **indentation**.
    *   **C**: Code structure is defined by `{}`; indentation is just for human readability.
    """)
    return


@app.cell
def _(print):
    x_8 = -5
    if x_8 > 0:
        print('x is positive')
    else:
        print('x is non-positive')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `else` block executes when the if condition is **False**.
    """)
    return


@app.cell
def _(print):
    x_9 = 0
    if x_9 > 0:
        print('x is positive')
    elif x_9 == 0:
        print('x is zero')
    else:
        print('x is negative')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *   `elif` → “else if”, checks additional conditions
    *   Multiple `elif` statements allowed
    """)
    return


@app.cell
def _(print):
    x_10 = 10
    y = 5
    if x_10 > 0 and y > 0:
        print('Both are positive')
    if x_10 > 0 or y < 0:
        print('At least one condition is True')
    if not y > 0:
        print('y is not positive')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key Takeaways**

    *   `if` → executes code when condition is **True**.
    *   `elif` → checks additional conditions if previous ones are **False**.
    *   `else` → executes when all previous conditions are **False**.
    *   Boolean operators (and, or, not) allow **complex logic**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div align="center">
      <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.scientecheasy.com%2Fwp-content%2Fuploads%2F2022%2F10%2Fflowchart-if-elif-else.png&f=1&nofb=1&ipt=f4561b36198c905ec86f8117787d9aade56e9b3dd1fe21f0f362a062d8ba83e7" height="900">
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `match-case`
    """)
    return


@app.cell
def _(print):
    command = "start"

    match command:
        case "start":
            print("Starting...")
        case "stop":
            print("Stopping...")
        case _:
            print("Unknown command")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A **modern alternative** ((introduced in Python 3.10)) to multiple `if-elif-else`, used for pattern matching.

    **Intuition**: “Check a variable against several possible values and run the first match.”
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Explanation**:

    *  `case "start":` - runs if `command == "start"`
    *  `_` - wildcard (like `else`)

    **Intuition**: “Match the first pattern that fits, otherwise do the default.”
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Match with Multiple Values**
    """)
    return


@app.cell
def _(print):
    day = "Saturday"

    match day:
        case "Saturday" | "Sunday":
            print("Weekend!")
        case _:
            print("Weekday")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Match with Patterns (Python 3.10+ advanced)**
    """)
    return


@app.cell
def _(print):
    point = (1, 0)
    match point:
        case [0, 0]:
            print('Origin')
        case [x_11, 0]:
            print(f'X-axis at {x_11}')
        case [0, y_1]:
            print(f'Y-axis at {y_1}')
        case [x_11, y_1]:
            print(f'Point at ({x_11}, {y_1})')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Intuition**: “You can match structures like tuples, lists, or objects.”
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `pass` and `...` (**Ellipsis**)
    """)
    return


@app.cell
def _(print):
    def describe_value(value):
        match value:
            case 0:
                print("Value is zero")
            case 1:
                pass  # Do nothing for value 1
            case 2:
                print("Value is two")
            case _:
                ...  # Ellipsis can act as a placeholder for future code

    # Usage examples
    describe_value(0)  # Output: Value is zero
    describe_value(1)  # Output: (nothing happens)
    describe_value(2)  # Output: Value is two
    describe_value(99) # Output: (nothing happens, Ellipsis used as placeholder)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Explanation**:

    * `pass`: Used to do nothing. It’s a placeholder for a case that currently requires no action.

    * `...` (**Ellipsis**): Can also be used as a placeholder, often signaling “**code to be implemented later**”.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ➿ Loops & Iterations in Python
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What Are Loops?

    Allow a program to repeat a block of code multiple times.

    **Intuition**: “Do this again and again until a condition is met.”
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The `while` loop
    """)
    return


@app.cell
def _(print):
    count = 0
    while count < 5:
        print('Count is:', count)
        count = count + 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Intuition**: “Keep doing this while the condition is true.”
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key points**:

    *   Make sure the condition will eventually become False to avoid an infinite loop.
    *   Can use break to exit early or continue to skip an iteration.

    <div style="text-align:center;">
      <img src="https://c.tenor.com/AP2-43cLmJMAAAAC/dormammu-doctor-strange.gif" height="200" style="margin-right:10px;">
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The `for` loop
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Repeats code **for each item in a sequence** (like a list, string, or range).
    """)
    return


@app.cell
def _(print):
    for i in range(5):
        print("i is:", i)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Intuition**: “Do this for every item in this list or range.”
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The `break` statement
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Stops the loop immediately, even if the condition hasn’t become **False**.
    """)
    return


@app.cell
def _(print):
    i_1 = 0
    while True:
        print(i_1)
        if i_1 == 3:
            break
        i_1 = i_1 + 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The `continue` statement
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Skips the rest of the current iteration and moves to the next one.
    """)
    return


@app.cell
def _(print):
    for i_2 in range(5):
        if i_2 == 2:
            continue
        print(i_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `else` with loops
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Optional: runs if the loop **completes normally** (not interrupted by `break`).
    """)
    return


@app.cell
def _(print):
    for i_3 in range(3):
        print(i_3)
    else:
        print('Loop finished without break')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Intuition**: “Do this if the loop wasn’t stopped early.”
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Iterations in Python: Lists, Sets, Tuples, Dicts & `zip`
    """)
    return


@app.cell
def _(print):
    # ======================================
    #               Lists
    print('Iteration over list')
    fruits_4 = ['apple', 'banana', 'cherry']
    for fruit in fruits_4:
        print(fruit)
    print()
    print()
    return


@app.cell
def _(print):
    # ======================================
    #                Sets
    print('Iteration over set')
    numbers_8 = {1, 2, 3, 2}
    for n in numbers_8:
        print(n)
    print()
    print()
    return


@app.cell
def _(print):
    # ======================================
    #                 Tuples
    print('Iteration over tuple')
    colors = ('red', 'green', 'blue')
    for color in colors:
        print(color)
    print()
    print()
    return


@app.cell
def _(print):
    # ======================================
    #               Dicts
    print('Iteration over dict')
    print('- using keys')
    person_2 = {'name': 'Pippo', 'age': 25}
    for key in person_2:
        print(key, ':', person_2[key])
    print()

    print('- using .items()')
    for key, value in person_2.items():
        print(key, ':', value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### The `zip()` function
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Combine multiple sequences into pairs/triples/...
    """)
    return


@app.cell
def _(print):
    names = ['Pippo', 'Bob', 'Charlie']
    ages = [25, 30, 35]

    for name, age_2 in zip(names, ages):
        print(name, 'is', age_2)
    return ages, names


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Intuition**: “Walk through multiple lists together.”
    """)
    return


@app.cell
def _(ages, names, print):
    ages.pop()
    print('length of names', len(names))
    print('length of ages', len(ages))
    print()

    for name_1, age_3 in zip(names, ages):
        print(name_1, 'is', age_3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `zip()` can be used to create dictionaries
    """)
    return


@app.cell
def _(print):
    keys = ['name', 'age', 'city']
    values = ['Pippo', 25, 'Paris']
    person_3 = dict(zip(keys, values))
    print(person_3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Intuition**: “Pair up items from two lists: first as keys, second as values.”
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Inline Comprehensions
    """)
    return


@app.cell
def _(print):
    squares = [x*x for x in range(5)]
    print("List:", squares)  # [0, 1, 4, 9, 16]

    unique = {x % 3 for x in range(10)}
    print("Set:", unique)  # {0, 1, 2}

    squares_dict = {x: x*x for x in range(5)}
    print("Dictionary:", squares_dict)  # {0:0, 1:1, 2:4, 3:9, 4:16}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 📐 Functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is a Function?

    A function is a block of reusable code that performs a specific task.

    Functions help to:

    *   **Organize code**
    *   **Avoid repetition**
    *   **Improve readability**

    **Intuition**: think of a function as a machine: you give it inputs, it processes them, and it returns an output.
    """)
    return


@app.cell
def _(print):
    def greet():
        print("Hello, world!")

    greet()
    return (greet,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *  `def` → keyword to define a function
    *  `greet` → function name
    *   `()` → parentheses for parameters (empty here)
    *  `:` → start of function body
    *  **Indentation** → required for the body of the function
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A function can be called any time after it has been defined:
    """)
    return


@app.cell
def _(greet):
    greet()  # Output: Hello, world!
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A function may accept parameters
    """)
    return


@app.cell
def _(print):
    def greet_name(name):
        print(f'Hello, {name}!')

    greet_name('Pippo')  # Output: Hello, Pippo!
    greet_name('Bob')  # Output: Hello, Bob!
    return (greet_name,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A function may return a value
    """)
    return


@app.cell
def _(print):
    def area_circle(radius):
        pi = 3.14159
        return pi * radius ** 2

    result = area_circle(5)
    print("Area:", result)   # Area: 78.53975
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Note**: Every function in Python returns a value. If no `return` statement is explicitly used, the function returns `None` by default.
    """)
    return


@app.cell
def _(greet_name, print):
    print(greet_name('Pluto'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A function may take multiple parameters and return more values
    """)
    return


@app.cell
def _(print):
    def rectangle_properties(length, width):
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter

    result_1 = rectangle_properties(10, 20)
    print('The whole result -->', result_1)
    print('The type of the result -->', type(result_1))
    return (rectangle_properties,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Note**: A function that returns multiple outputs returns a tuple containing the resulting values.
    """)
    return


@app.cell
def _(print, rectangle_properties):
    area_1, perimeter = rectangle_properties(10, 20)
    print('Area:', area_1)
    print('Perimeter:', perimeter)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A function may also have some parameters with default values
    """)
    return


@app.cell
def _(print):
    def rectangle_properties_1(length, width=3):
        area = length * width
        perimeter = 2 * length + width
        return (area, perimeter)

    area_2, perimeter_1 = rectangle_properties_1(10)
    print('Area:', area_2)
    print('Perimeter:', perimeter_1)
    return (rectangle_properties_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Arguments can be passed using keywords, allowing the parameter order to be ignored
    """)
    return


@app.cell
def _(print, rectangle_properties_1):
    area_3, perimeter_2 = rectangle_properties_1(10, 20)
    print('Area:', area_3)
    print('Perimeter:', perimeter_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All positional arguments must come before any keyword arguments
    """)
    return


@app.cell
def _(print, rectangle_properties_1):
    area_4, perimeter_3 = rectangle_properties_1(width=10, length=20)
    print('Area:', area_4)
    print('Perimeter:', perimeter_3)
    return


app._unparsable_cell(
    r"""
    area, perimeter = rectangle_properties(length=10, 20)

    print("Area:", area)
    print("Perimeter:", perimeter)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Local Vs Global Scope
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What Is the Context of a Function?

    The context (or scope) of a function refers to where variables and functions are visible and accessible.

    Python has nested scopes:

    *   **Local scope** – inside the function
    *   **Enclosing scope** – outer functions if nested
    *   **Global scope** – outside all functions
    *   **Built-in scope** – Python’s built-in names
    """)
    return


@app.cell
def _(print):
    x_12 = 10  # global variable
    print('Before the function: x =', x_12)
    return (x_12,)


@app.cell
def _(print, x_12):
    def my_function(x):
        x = x + 5
        z = 5  # local variable
        print('Inside function: x =', x, 'z =', z)  # local variable

    my_function(x_12)
    return


@app.cell
def _(print, z):
    print(z)  # ❌ NameError: z is not accessible here
    return


@app.cell
def _(print, x_12):
    print('Outside function: x =', x_12)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `global` allows the function to access and modify the variable in the global scope
    """)
    return


@app.cell
def _(print):
    counter = 0  # global variable

    def increment():
        global counter  # declare that we want to modify the global variable
        counter = counter + 1
    increment()
    print(counter)  # Output: 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Nested Functions
    """)
    return


@app.cell
def _(print):
    def outer_function(x):
        def inner_function(y):
            return y ** 2

        result = inner_function(x) + 5
        return result

    print(outer_function(3))  # Output: 14
    return


@app.cell
def _(inner_function, print):
    print(inner_function(3))  # Output: NameError: name 'inner_function' is not defined
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key Takeaways**:

    *   Nested functions help **organize code** and avoid polluting the global namespace
    *   Inner functions can **access outer function variables** (closure)
    *   They are useful in larger programs or functional programming patterns
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### **PEP 8 Tips**:
    *   Use **snake_case** for function names: `calculate_area`, not `CalculateArea`.
    *   Keep functions **short and focused** (do one thing well).
    *   Use docstrings (`\"\"\"...\"\"\"`) to explain what the function does.
    *   Use **type hints** for parameters and return values.
    *   Always specify `return None`.
    """)
    return


@app.cell
def _(help):
    def area_circle_1(radius: float) -> float:
        """Return the area of a circle given its radius.

        Args:
            radius (float): The radius of the circle.

        Returns:
            float: The area of the circle.
        """
        pi: float = 3.14159  # This is a docstring, it can be called by the help method
        return pi * radius ** 2


    help(area_circle_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## λ Lambda Functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is a Lambda Function?

    A **lambda function** is **a small, anonymous function** defined without a name.

    *   Can have any number of inputs, but only one expression.

    Syntax:

    ```python
    lambda arguments: expression
    ```

    **Key Properties**:

    *   Returns the result of the expression automatically
    *   Often used as short, inline functions
    *   Commonly used with functions like `map()`, `filter()`, and `sorted()`
    """)
    return


@app.cell
def _(print):
    # Traditional function
    def square(x):
        return x ** 2

    # Lambda function equivalent
    square_lambda = lambda x: x ** 2

    print('Traditional Function -->', square(5))
    print('Lambda Function -->', square_lambda(5))  # Output: 25
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using Lambda with `map()` and `filter()`
    """)
    return


@app.cell
def _(print):
    numbers_9 = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers_9))
    # Square all numbers using map
    print(squared)
    evens = list(filter(lambda x: x % 2 == 0, numbers_9))  # [1, 4, 9, 16, 25]
    # Filter even numbers using filter
    print(evens)  # [2, 4]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `map()`

    *  Applies a function to every element in an iterable (like a list)
    *   Returns a map object, which can be converted to a list

    `filter()`

    *   Selects elements from an iterable that satisfy a condition
    *   Returns a filter object, which can be converted to a list
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🏭 Generators
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is a Generator?

    *  A **generator** is a special type of function that remembers its state between calls.
    *  Instead of returning all results at once, it **produces values one at a time** (lazy evaluation).
    *  More **memory-efficient** than lists for large sequences.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `yield` Keyword

    *   Works like `return`, but instead of ending the function, it pauses it.
    *   The function can then **resume where it left off**.
    """)
    return


@app.cell
def _():
    def count_up_to(n):
        i = 1
        while i <= n:
            yield i  # pause and return i
            i = i + 1

    jhin_counter = count_up_to(4)

    type(jhin_counter)
    return (jhin_counter,)


@app.cell
def _(jhin_counter, print):
    print(next(jhin_counter))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Inline Comprehension
    """)
    return


@app.cell
def _(print):
    cubes = (x**3 for x in range(5))
    print(cubes)

    for cube in cubes:
        print(cube)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Difference in "per-for-mAHns"
    """)
    return


@app.cell
def _(print):
    import sys

    # List comprehension
    lst = list(range(1_000_000))
    print("List memory:", sys.getsizeof(lst), "bytes")

    # Generator expression
    gen = (x for x in range(1_000_000))
    print("Generator memory:", sys.getsizeof(gen), "bytes")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key Takeaways**

    *   **Generator** = **function** + `yield`
    *   Produces values **lazily** (one by one)
    *   Efficient for **big or infinite data**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🗃️ Classes
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is a Class?

    A class is a blueprint for creating objects.

    *   Encapsulates data (**attributes**) and functions (**methods**).
    *   Objects are instances of a class.

    **Intuition**: A class is like a blueprint for a house; objects are the actual houses built from it.
    """)
    return


@app.cell
def _(help, print):
    class Person:
        """A simple class representing a person.""" # The docstring describing the class

        def __init__(self, name, age, height_in_m, is_student=False):
            self.user_name = name   # attribute
            self.age = age          # attribute
            self.height_in_m = height_in_m  # attribute
            self.is_student = is_student    # attribute

        def greet(self):
            print(f"Hello, my name is {self.user_name} and I am {self.age} years old.")

    help(Person)
    return (Person,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Explanation**:

    *   `__init__` → constructor, called when creating a new object
    *  `self` → reference to the current object
    * `name` and `age` → attributes
    * `greet()` → method
    """)
    return


@app.cell
def _(Person):
    pippo_1 = Person('Pippo', 25, height_in_m=1.75)
    bob = Person('Bob', 30, 1.75, True)
    pippo_1.greet()
    bob.greet()  # Hello, my name is Pippo and I am 25 years old.  # Hello, my name is Bob and I am 30 years old.
    return (pippo_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Modifying Attributes
    """)
    return


@app.cell
def _(pippo_1, print):
    pippo_1.age = 26
    print(pippo_1.age)  # 26
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Magic Methods
    """)
    return


@app.cell
def _(help, print):
    class Person_1:
        """A simple class representing a person."""  # The docstring describing the class

        def __init__(self, name, age, height_in_m, is_student=False):
            self.user_name = name  # attribute
            self.age = age  # attribute
            self.height_in_m = height_in_m  # attribute
            self.is_student = is_student  # attribute

        def greet(self):
            print(f'Hello, my name is {self.user_name} and I am {self.age} years old.')

        def __len__(self):  # In this case, it returns the age
            return self.age

        def __str__(self):
            description = f'GENERAL ID:\n        - name : {self.user_name}\n        - age : {self.age}\n        - height (meters): {self.height_in_m}\n        - student: {self.is_student}\n        '
            return description

    help(Person_1)
    return (Person_1,)


@app.cell
def _(Person_1, print):
    pippo_2 = Person_1('Pippo', 25, height_in_m=1.75)
    bob_1 = Person_1('Bob', 30, 1.75, True)
    print(len(pippo_2))
    print(len(bob_1))
    print()
    print(pippo_2)
    print(bob_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key Points**

    *   **Special methods** (also called “magic methods”) allow Python objects to **interact with built-in functions and operators**.
    *   They follow the double underscore naming convention: `__method__`.

    Using them allows **custom behavior** for:

    *   Built-in functions (`len()`, `str()`)
    *   Operators (`+`, `*`, `==`)
    *   Attribute access (`__get__`, `__set__`)
    *   etc...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For further reading, see [Real Python](https://realpython.com/python-magic-methods/) and [GeeksforGeeks](https://www.geeksforgeeks.org/python/dunder-magic-methods-python/)...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Inheritance in Python
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is Inheritance?

    Inheritance allows a class (child/subclass) to **reuse attributes and methods from another class** (parent/superclass).

    *   Promotes code reuse, organization, and extensibility.

    **Intuition**: A child class **inherits traits** from its parent class but can also add or override features.
    """)
    return


@app.cell
def _(print):
    # Parent class
    class Animal:

        def __init__(self, name):
            self.name = name

        def speak(self):
            print(f'{self.name} makes a sound.')
    # Child class

    class Dog(Animal):

        def speak(self):
            print(f'{self.name} barks.')
    a_5 = Animal('Generic Animal')  # Generic Animal makes a sound.
    a_5.speak()
    d = Dog('Buddy')
    d.speak()  # Buddy barks.
    return (Animal,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Explanation**:

    *   Dog **inherits** from Animal
    *   Can **override** the `speak()` method
    *   Inherits `__init__` automatically (or can define its own)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Using `super()`
    """)
    return


@app.cell
def _(Animal, print):
    class Dog_1(Animal):

        def __init__(self, name, breed):
            # Call parent constructor
            super().__init__(name)
            self.breed = breed

        def speak(self):
            print(f'{self.name} the {self.breed} barks.')


    d_1 = Dog_1('Buddy', 'Labrador')
    d_1.speak()  # Buddy the Labrador barks.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Explanation**:

    *   `super()` calls the parent class method, useful for extending functionality
    *   Avoids rewriting parent initialization
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key Takeaways**

    *   Inheritance allows c**ode reuse and extension**
    *   Child classes can **override** or **extend** parent methods
    *   Use `super()` to **call parent methods safely**
    *   Supports **polymorphism**: same method name can behave differently in subclasses
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Private Attributes and Methods in Python
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python does not enforce strict privacy, but uses naming conventions to indicate “internal use”
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | Prefix      | Meaning                                                              |
    | ----------- | -------------------------------------------------------------------- |
    | `_single`   | Intended as **protected** (internal use, not enforced)               |
    | `__double`  | Triggers **name mangling** → harder to access from outside the class |
    | `no prefix` | Public attribute or method (accessible everywhere)                   |
    """)
    return


@app.cell
def _(print):
    class Person_2:

        def __init__(self, name, age):
            self._name = name # protected, internal use
            self.age = age # public

        # Protected Method
        def _greet(self):
            print(f'Hello, my name is {self._name}')


    p = Person_2('Pippo', 25)
    print(p.age)  # 25 (public)
    p._greet()  # works, but intended as internal
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Explanation**:

    *   `_name` and `_greet()` are intended for internal use

    *   Can still be accessed, but by convention, users shouldn’t
    """)
    return


@app.cell
def _(print):
    class Person_3:

        def __init__(self, name, age):
            self.__name = name # private attribute

        # Private Method
        def __greet(self):
            print(f'Hello, my name is {self.__name}')

    p_1 = Person_3('Bob', 30)

    print(p_1.__name)  # ❌ AttributeError
    p_1.__greet()  # ❌ AttributeError
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Explanation**:

    *   `__name` and `__greet()` are name-mangled → harder to access from outside

    *   Helps prevent accidental overriding in subclasses
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key Points**:

    *   **Private attributes** are often used with `@property` to control access and validation.

    *   **Protected attributes** can also use properties if you want controlled access, though they are more “internal use” by convention.

    *   **Properties** allow **encapsulation** without changing how the attribute is accessed externally (`obj.attr` syntax).

    *   This combination gives you the best of both worlds: hiding the internal representation while providing safe access.

    or more information on using protected and private attributes with properties, see this guide: [Python Property Decorator](https://www.freecodecamp.org/news/python-property-decorator/).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🛠️ Error Handling
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Why Error Handling?

    *   Errors (exceptions) occur during program execution.
    *   Without handling, the program **stops abruptly**.
    *   Error handling allows your program to **respond gracefully**.
    """)
    return


@app.cell
def _(input):
    number_input_1 = input('Enter a number:', 'abc')
    number_input_1
    return (number_input_1,)


@app.cell(hide_code=True)
def _(number_input_1, print):
    try:
        x_13 = int(number_input_1.value)
        print('You entered:', x_13)
    except ValueError:
        print('Oops! That was not a valid number.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Explanation**:

    *   `try` → code that might raise an error
    *   `except` → code that runs if an exception occurs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can catch specific exceptions and not others
    """)
    return


@app.cell
def _(print):
    try:
        result_2 = 10 / 0
    except ZeroDivisionError:
        print('Cannot divide by zero!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tip**: Always catch specific exceptions rather than using a bare `except:`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Using `else` and `finally`
    """)
    return


@app.cell
def _(input):
    number_input_2 = input('Enter a number:', '42')
    number_input_2
    return (number_input_2,)


@app.cell(hide_code=True)
def _(number_input_2, print):
    try:
        x_14 = int(number_input_2.value)
    except ValueError:
        print('Invalid input!')
    else:
        print('Input is valid, you entered:', x_14)
    finally:
        print('This runs no matter what!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *   `else` → executes if **no exception** occurred
    *   `finally` → executes **always**, useful for cleanup
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Raising Exceptions
    """)
    return


@app.cell
def _(input):
    command_1 = input('Enter a command:', 'pass')
    command_1
    return (command_1,)


@app.cell
def _(command_1, print):
    match command_1.value:
        case 'start':
            print('Starting...')
        case 'stop':
            print('Stopping...')
        case _:
            raise Exception('Unknown command')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *   `raise` lets you manually trigger an exception
    *   Useful for validating inputs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The `assert` Statement in Python
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What is `assert`?

    *   `assert` is used to **check if a condition is True**.
    *   If the condition is **False**, Python raises an `AssertionError`.
    * Useful for d**ebugging and validating assumptions** during development.
    """)
    return


@app.cell
def _():
    x_15 = 5
    assert x_15 > 0  # Passes, no error
    assert x_15 < 0, 'Cannot go below zero.'  # ❌ Raises AssertionError
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key Takeaways**

    *   Use `try-except` to prevent crashes
    *   Catch **specific exceptions** when possible
    *   Use `else` for code that should run only if no error occurred
    *   Use `finally` for **cleanup actions**
    *   Use `raise` to **signal errors manually**
    *   `assert` helps document assumptions in the code
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 📚 References
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### General References
    *  [Real Python](https://realpython.com/)
    *  [Real Python - Data Science](https://realpython.com/tutorials/data-science/)
    *  [Real Python - Installing Python](https://realpython.com/installing-python/)
    *  [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)
    *  [freeCodeCamp Data Science](https://www.freecodecamp.org/news/learn-python-for-data-science-full-course/)
    *  [Indently Youtube Channel](https://www.youtube.com/@Indently)
    * [CalmCode Youtube Channel](https://www.youtube.com/@calmcode-io)

    ### Environments
    *  [pip](https://python.land/virtual-environments/virtualenv): The standard tool for creating virtual environments for individual projects.
    *  [Anaconda or conda](https://www.anaconda.com/docs/getting-started/working-with-conda/environments): Allows you to create reusable environments across multiple projects.
    *  [uv](https://docs.astral.sh/uv/getting-started/): An alternative to pip that lets you quickly and easily create project-specific environments—simple, intuitive, and batteries included.

    A [great blog post](https://janakiev.com/blog/jupyter-virtual-envs/) explaining how to create virtual environments (`pip` or `conda`) and connect them to a Jupyter kernel. Here a [guide](https://docs.astral.sh/uv/guides/integration/jupyter/) for doing the same using `uv`.

    ### Personal Suggestions

    *   from [VScode](https://code.visualstudio.com/) to [Zed](https://zed.dev/).
    *   from [pandas](https://pandas.pydata.org/docs/) to [polars](https://docs.pola.rs/api/python/stable/reference/index.html).
    *   visualization libraries ([seaborn](https://seaborn.pydata.org/), [plotly](https://plotly.com/python/), [plotnine](https://plotnine.org/), [lets-plot](https://lets-plot.org/))
    * from jupyter notebooks to [marimo](https://marimo.io/)
    *  for python environments [uv](https://docs.astral.sh/uv/) (a [Medium guide](https://medium.com/@vkmauryavk/managing-python-virtual-environments-with-uv-a-comprehensive-guide-ac74d3ad8dff))

    ### Can be handy for later...

    *   [A guide to pytorch](https://www.youtube.com/watch?v=Z_ikDlimN6A&t=2570s)
    *   [Pytorch Lighting](https://pytorch-lighting.readthedocs.io/en/latest/)
    *   [Weights & Biases](https://wandb.ai/site)
    *   [Hydra](https://www.sscardapane.it/tutorials/hydra-tutorial/)
    *   [Just](https://just.systems/man/en/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 👐 Thanks & Have Fun Coding!

    <div align="center">
      <img src="https://i.programmerhumor.io/2023/06/programmerhumor-io-python-memes-backend-memes-6e51e8ccc5a8207.jpg" width="500">
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
