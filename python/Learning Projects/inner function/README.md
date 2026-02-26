![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Closures%20%7C%20Scope%20%7C%20nonlocal-f59e0b?style=flat)

# 🔒 Inner Functions — Closures and Scope

A focused demonstration of Python's nested function mechanics: how inner functions access variables from an enclosing scope (closure), and how the `nonlocal` keyword enables an inner function to _modify_ those variables rather than just read them.

---

## Overview

Understanding closures and scope is essential for working with decorators, factory functions, callback patterns, and async code. This exercise isolates the key mechanics in the simplest possible example.

---

## Concepts Demonstrated

- Nested (inner) function definition
- Closures — the inner function "closes over" a variable from the outer scope
- The `nonlocal` keyword — required when an inner function needs to _reassign_ (not just read) an enclosing variable
- Python's LEGB scope resolution order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

---

## How It Works

```python
def outer_func():
    msg = 'Hello there!'   # Enclosing scope variable
    res = ""               # Declared here so inner_func can modify it

    def inner_func():
        nonlocal res       # Tells Python: "res" lives in the enclosing scope
        res = 'How are you?'
        print(msg)         # Read from enclosing scope — works without nonlocal

    inner_func()
    print(res)             # Now reflects the value set by inner_func

outer_func()
```

**Output:**
```
Hello there!
How are you?
```

---

## Why `nonlocal` Is Needed

Without `nonlocal`, assigning `res = 'How are you?'` inside `inner_func` would create a _new local variable_ named `res`, leaving the outer `res` unchanged. `nonlocal` explicitly binds the name to the enclosing scope.

| Action | Needs `nonlocal`? |
|---|---|
| Reading `msg` from outer scope | No |
| Reassigning `res` in outer scope | Yes |
| Modifying a mutable object (e.g., `list.append`) | No |

---

## Skills Demonstrated

- Understanding Python's scope resolution rules (LEGB)
- Writing inner functions that interact cleanly with their enclosing context
- Using `nonlocal` correctly — the pattern behind many decorator implementations
- Foundational knowledge for building closures, memoisation, and factory functions

---

## Technologies

- Python 3 (no external libraries)

---

## 🔗 Back

[← Learning Projects](../README.md) | [← Main README](../../../README.md)
