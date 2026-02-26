![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-OOP%20%7C%20Attribute%20Introspection-8b5cf6?style=flat)

# 🔍 Classes and Objects — Dynamic Attribute Management

A set of five focused exercises exploring Python's built-in object introspection functions: `setattr`, `getattr`, `hasattr`, and `delattr`. Each file isolates one function, and `all in one.py` combines all four into an interactive command-line application.

---

## Overview

Python allows you to read, write, check, and delete object attributes at runtime using four built-in functions. This capability powers frameworks like Django (which dynamically assigns model fields) and is essential for writing flexible, generic code.

---

## Files

| File | Function Demonstrated | Description |
|---|---|---|
| `dinamically get attribute.py` | `getattr` | Read an attribute by name at runtime |
| `din set attribute.py` | `setattr` | Write/update an attribute by name at runtime |
| `has attribute.py` | `hasattr` | Check whether an attribute exists before accessing |
| `delete attribute.py` | `delattr` | Remove an attribute from an object at runtime |
| `all in one.py` | All four | Interactive CLI combining all operations |

---

## Concepts Demonstrated

- `setattr(obj, name, value)` — dynamically set any attribute
- `getattr(obj, name, default)` — safely retrieve an attribute value
- `hasattr(obj, name)` — guard against AttributeError before access
- `delattr(obj, name)` — remove an attribute at runtime
- Python's `__dict__` — the underlying dictionary of an object's attributes
- Interactive CLI loop with branching input handling

---

## How It Works

```python
class Student:
    def __init__(self, name):
        self.name = name

student = Student("John")

# Dynamically add a new attribute
setattr(student, "age", 25)

# Safely retrieve it
print(getattr(student, "age", "not found"))  # → 25

# Check before deleting
if hasattr(student, "age"):
    delattr(student, "age")

# Inspect all attributes
print(student.__dict__)  # → {'name': 'John'}
```

---

## Skills Demonstrated

- Understanding Python's object model at the attribute level
- Writing defensive code that checks existence before access
- Using runtime introspection — a pattern found throughout Django, DRF, and Python ORMs
- Building interactive CLI programs with clear user feedback

---

## Technologies

- Python 3 (no external libraries)

---

## 🔗 Back

[← Learning Projects](../README.md) | [← Main README](../../../README.md)
