# Week 6 Assignment - Safe Functions

`safe_tools.py` contains three functions that safely handle division, integer
conversion, and dictionary field lookup.

`README.md` describes the assignment and explains why invalid number input
requires exception handling.

An `if` check alone does not convert text or catch conversion errors. When
`int()` receives text such as `"abc"`, it raises a `ValueError`; using
`try/except` lets the program handle that error safely.