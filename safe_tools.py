"""Examples of handling common errors safely.

safe_divide calculates a / b and returns a message if b is zero.
safe_number converts numeric text to an integer and handles invalid text.
get_field retrieves a learner dictionary value and handles missing keys.
The examples below show both successful and error cases.

Run from this file's folder with:
    python safe_tools.py
or, if needed:
    python3 safe_tools.py

Expected output:
    5.0
    Cannot divide by zero
    42
    Not a number
    82
    Field not found
"""


def safe_divide(a, b):
    """Return a / b, or a message if the divisor is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def safe_number(text):
    """Return text as an integer, or a message if it is not a valid integer."""
    try:
        return int(text)
    except ValueError:
        return "Not a number"


def get_field(learner, key):
    """Return the value for key, or a message if the key is missing."""
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))