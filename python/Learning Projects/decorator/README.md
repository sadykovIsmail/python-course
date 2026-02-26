![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Decorators%20%7C%20Closures-f59e0b?style=flat)

# 🎁 Decorator — Function Wrapping from Scratch

A minimal but complete implementation of a Python decorator built without using `@` syntax. The decorator wraps a greeting function and transforms its return value to uppercase, demonstrating exactly what happens under the hood when Python processes `@decorator_name`.

---

## Overview

Decorators are one of Python's most powerful features. They are used extensively in Django (`@login_required`, `@property`), DRF (`@api_view`, `@permission_classes`), and standard Python (`@staticmethod`, `@classmethod`). Understanding how they work from first principles makes reading and writing framework code significantly easier.

---

## Concepts Demonstrated

- Higher-order functions (functions that accept or return other functions)
- Closures — the `wrapper` function captures the original function in its scope
- Function composition and transparent wrapping
- The equivalence between `@decorator` syntax and manual assignment

---

## How It Works

```python
def say_hello():
    name = input('What is your name? ')
    return 'Hello ' + name

def uppercase_decorator(func):
    def wrapper():
        result = func()           # Call the original function
        return result.upper()     # Transform its output
    return wrapper                # Return the wrapper, not the result

# Manual decoration — equivalent to @uppercase_decorator
say_hello = uppercase_decorator(say_hello)

print(say_hello())  # → "HELLO JOHN"
```

**What `@uppercase_decorator` does at import time:**
1. Calls `uppercase_decorator(say_hello)`
2. Returns the `wrapper` function
3. Binds `say_hello` to `wrapper`

Every subsequent call to `say_hello()` runs `wrapper()`, which internally calls the original function and transforms its output.

---

## Example Output

```
What is your name? Ismail
HELLO ISMAIL
```

---

## Skills Demonstrated

- Building decorators from scratch without syntactic sugar
- Understanding closures and how inner functions capture enclosing scope
- Recognising the pattern used by all Python framework decorators
- Writing reusable, non-destructive function wrappers

---

## Technologies

- Python 3 (no external libraries)

---

## 🔗 Back

[← Learning Projects](../README.md) | [← Main README](../../../README.md)
