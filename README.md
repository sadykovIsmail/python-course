![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Algorithms](https://img.shields.io/badge/Algorithms-12%2B%20Implemented-22c55e?style=flat)
![Data Structures](https://img.shields.io/badge/Data%20Structures-Linked%20List%20%7C%20Hash%20Table%20%7C%20Graph-f59e0b?style=flat)
![OOP](https://img.shields.io/badge/OOP-Classes%20%7C%20Inheritance%20%7C%20Patterns-8b5cf6?style=flat)
![Backend Engineering](https://img.shields.io/badge/Backend%20Engineering-Django%20Ready-ef4444?style=flat)
![License](https://img.shields.io/badge/License-MIT-6b7280?style=flat)

# 🐍 Python Engineering Practice Repository

A structured, hands-on Python learning portfolio built while actively transitioning into backend engineering. This repository progresses from core Python fundamentals through object-oriented design, custom data structures, algorithm implementation, and software engineering patterns — the exact skill stack required for professional backend development with Django and Django REST Framework.

Every project here solves a real problem and is written with production habits in mind: input validation, encapsulation, single responsibility, and clean interfaces.

---

## 🎯 Purpose

This repository was created to master Python as the primary language for backend engineering and software development. Every project here reflects real problem-solving practice, deliberately chosen to build the skills required for professional backend work with frameworks like Django and Django REST Framework.

---

## 🚀 Skills Demonstrated

| Category | Topics Covered |
|---|---|
| **Core Python** | syntax, functions, closures, comprehensions, string manipulation |
| **Data Structures** | linked lists, hash tables, graphs (adjacency matrix & list) |
| **Algorithms** | binary search, merge sort, quick sort, selection sort, bisection method, Tower of Hanoi, Luhn checksum |
| **Object-Oriented Programming** | classes, inheritance, encapsulation, polymorphism, dunder methods |
| **Design Patterns** | Strategy pattern, Abstract Base Classes, object composition |
| **Data Validation** | regex validation, checksum algorithms, type enforcement, constraint checking |
| **Software Engineering** | modular design, defensive programming, single-responsibility functions, custom exceptions |

---

## 📁 Repository Structure

```
python-course/
│
├── README.md                              ← You are here
│
└── python/
    ├── Learning Projects/                 ← Focused concept exercises
    │   ├── classes and objects/           ← Dynamic attribute introspection
    │   │   ├── all in one.py              ← Interactive CLI (setattr/getattr/hasattr/delattr)
    │   │   ├── delete attribute.py
    │   │   ├── din set attribute.py
    │   │   ├── dinamically get attribute.py
    │   │   └── has attribute.py
    │   ├── decorator/
    │   │   └── decorator.py               ← Custom function decorator from scratch
    │   ├── graphs/
    │   │   └── 1.py                       ← Adjacency matrix & adjacency list
    │   └── inner function/
    │       └── inner.py                   ← Closures and the nonlocal keyword
    │
    └── Professional Projects/             ← Applied, project-scale exercises
        ├── 0.hello world.py
        ├── 1. caesar_clipher.py           ← Encryption with str.maketrans
        ├── 2. rpg character.py            ← Input validation & formatted output
        ├── 3. pin extractor.py            ← Text parsing & nested iteration
        ├── 4. numbet pattern generator.py
        ├── 5. medical data validation.py  ← Regex + dict validation pipeline
        ├── 6.user configuration manager.py
        ├── 7. isbn validator.py           ← ISBN-10 & ISBN-13 checksum algorithms
        ├── 8.musical instriment inventory.py
        ├── 9.planet class.py
        ├── 10. email simulator.py         ← Multi-class OOP + datetime
        ├── 11. budget app.py              ← Ledger system + ASCII chart
        ├── 12. salary tracker.py          ← @property + business rule enforcement
        ├── 13. game character.py          ← Value clamping with property setters
        ├── 14. media catalogue app.py     ← Inheritance + custom exceptions
        ├── 15. discount calculator.py     ← Strategy design pattern + ABC
        ├── 16. Player interface.py        ← Abstract base class + random movement
        ├── 17.polygon area calculator.py  ← Geometric class hierarchy
        ├── 18. linked list.py             ← Singly linked list from scratch
        ├── 19. hash table.py              ← Custom hash function + collision chaining
        ├── 20. binary search.py           ← O(log n) search with path tracking
        ├── 21. bisection method.py        ← Numerical square root approximation
        ├── 22. merge sort.py              ← Divide-and-conquer O(n log n) sort
        ├── 23. quick sort.py              ← Pivot-based recursive sort
        ├── 24. selection sort.py          ← In-place O(n²) sort
        ├── 25. Luhn algorithm.py          ← Credit card checksum validation
        └── 25. tower of hanoi.py          ← Recursive puzzle solver
```

---

## 📊 Algorithms Implemented

| Algorithm | Category | Time Complexity | File |
|---|---|---|---|
| Binary Search | Search | O(log n) | `20. binary search.py` |
| Merge Sort | Sorting | O(n log n) | `22. merge sort.py` |
| Quick Sort | Sorting | O(n log n) avg / O(n²) worst | `23. quick sort.py` |
| Selection Sort | Sorting | O(n²) | `24. selection sort.py` |
| Bisection Method | Numerical | O(log n) | `21. bisection method.py` |
| Tower of Hanoi | Recursion | O(2ⁿ) | `25. tower of hanoi.py` |
| Luhn Algorithm | Validation | O(n) | `25. Luhn algorithm.py` |
| ISBN-10 Checksum | Validation | O(n) | `7. isbn validator.py` |
| ISBN-13 Checksum | Validation | O(n) | `7. isbn validator.py` |
| Caesar Cipher | Cryptography | O(n) | `1. caesar_clipher.py` |

---

## 🧠 Concepts Practiced

**Foundations**
- Python syntax, built-in types, and control flow
- Functions, default arguments, and optional parameters
- String manipulation, f-strings, and translation tables

**Data Structures**
- Lists, dictionaries, sets, and tuples
- Singly linked list (custom implementation)
- Hash table with collision chaining (custom implementation)
- Graphs: adjacency matrix and adjacency list representations

**Object-Oriented Programming**
- Class definition, `__init__`, instance and class attributes
- Dunder methods: `__str__`, `__repr__`
- Inheritance and `super().__init__()`
- Encapsulation with `@property` getters and setters
- Polymorphism and method overriding
- Abstract Base Classes (`ABC`) and `@abstractmethod`
- Custom exception classes
- Object composition

**Design Patterns**
- Strategy pattern (discount engine)
- Template method (abstract player interface)
- Decorator pattern (function wrapping)

**Data Validation & Algorithms**
- Regex validation with `re.fullmatch`
- Checksum algorithms (Luhn, ISBN-10, ISBN-13)
- Recursive divide-and-conquer
- Numerical methods (bisection / interval halving)
- Input type and range enforcement

**Closures & Scoping**
- Inner functions and closures
- The `nonlocal` keyword
- LEGB scope resolution

---

## 📂 Projects and Exercises

### 📁 Learning Projects

---

### Classes and Objects — Dynamic Attribute Management

A set of focused exercises exploring Python's built-in object introspection tools. Covers how to dynamically read, write, check, and remove attributes on class instances at runtime — a pattern commonly used in frameworks and ORMs. The `all in one.py` file brings these together into an interactive CLI.

**Key concepts:**
- `setattr` / `getattr` / `hasattr` / `delattr`
- Runtime object mutation
- Interactive command-line interface

**Skills demonstrated:**
- Understanding Python's object model
- Dynamic property management
- Writing defensive code with existence checks

---

### Decorator

Implements a custom function decorator that wraps a greeting function and transforms its output to uppercase. Demonstrates the fundamentals of higher-order functions and closures that power Python's `@decorator` syntax.

**Key concepts:**
- Higher-order functions
- Closures and function wrapping
- The decorator pattern

**Skills demonstrated:**
- Writing reusable function wrappers
- Understanding Python's execution model
- Applying the decorator pattern from scratch

---

### Graphs

Explores two fundamental graph representations: the adjacency matrix and the adjacency list. Provides a clear side-by-side comparison of how the same graph topology can be stored differently depending on performance requirements.

**Key concepts:**
- Graph data structures
- Adjacency matrix vs. adjacency list
- Space vs. time trade-offs

**Skills demonstrated:**
- Modelling relationships between nodes
- Choosing appropriate data representations
- Foundation for BFS/DFS traversal algorithms

---

### Inner Functions

Demonstrates how inner (nested) functions work in Python, including variable scope, closures, and the `nonlocal` keyword to allow inner functions to modify variables in an enclosing scope.

**Key concepts:**
- Nested function definitions
- Closures and lexical scoping
- `nonlocal` keyword

**Skills demonstrated:**
- Managing variable scope deliberately
- Writing encapsulated helper functions
- Understanding Python's LEGB scope rules

---

### 📁 Professional Projects

---

### 0. Hello World

The starting point of the repository. Two simple functions demonstrate basic Python function definition, calling, and string composition.

**Key concepts:**
- Function definition and invocation
- String concatenation
- Entry-level Python syntax

**Skills demonstrated:**
- Writing and calling functions
- Understanding program flow
- Clean, minimal code structure

---

### 1. Caesar Cipher

Implements a classic encryption algorithm that shifts each letter in a string by a given number of positions. Supports both encryption and decryption by reversing the shift. Uses `str.maketrans` for efficient character mapping.

**Key concepts:**
- String manipulation and translation tables
- `str.maketrans` and `str.translate`
- Input validation with type and range checks
- Conditional logic for encrypt/decrypt modes

**Skills demonstrated:**
- Implementing classical cryptography in Python
- Working with character encodings
- Writing functions with optional parameters and guards

---

### 2. RPG Character Creator

Builds an RPG character with a name and three stats (strength, intelligence, charisma) that must sum to exactly 7. Renders the character sheet with filled and empty dot symbols for a visual stat display.

**Key concepts:**
- Input validation and constraint enforcement
- F-string formatting
- Type checking with `isinstance`
- Visual output construction

**Skills demonstrated:**
- Defensive programming with clear error messages
- Producing formatted terminal output
- Implementing game-logic rules in code

---

### 3. PIN Extractor

Extracts hidden secret codes from poems by reading the length of specific words at specific line positions. Processes multiple poems using nested string operations.

**Key concepts:**
- String splitting and indexing
- Nested loops
- List accumulation and enumeration
- Edge case handling

**Skills demonstrated:**
- Parsing structured text programmatically
- Working with multi-dimensional iteration
- Writing clean, readable algorithmic logic

---

### 4. Number Pattern Generator

Generates a space-separated string of numbers from 1 to n, with full input validation. Includes both an explicit loop version and an optimised generator expression version for comparison.

**Key concepts:**
- Loop-based vs. generator-based string building
- `str.join` and generator expressions
- Input validation

**Skills demonstrated:**
- Writing clean, idiomatic Python
- Refactoring from explicit to optimised implementations
- Recognising trade-offs between verbosity and brevity

---

### 5. Medical Data Validation

Validates a list of patient medical records against strict format rules using regular expressions. Checks patient IDs, age ranges, gender values, medication lists, and visit IDs. Reports specific fields that fail validation.

**Key concepts:**
- Regular expressions (`re.fullmatch`, `re.IGNORECASE`)
- Dictionary validation and key-set comparison
- `isinstance` checks for nested types
- Reporting errors with positional context

**Skills demonstrated:**
- Data validation patterns used in real backend systems
- Working with the `re` module
- Writing clear, structured validation pipelines

**Technologies / libraries used:**
- `re`

---

### 6. User Configuration Manager

A CRUD-style key-value settings manager backed by a dictionary. Supports adding, updating, deleting, and viewing user configuration entries, with duplicate key protection and case-normalisation on all keys and values.

**Key concepts:**
- Dictionary CRUD operations
- Key normalisation and deduplication
- Formatted multi-line output

**Skills demonstrated:**
- Implementing simple in-memory stores
- Writing modular, single-responsibility functions
- Pattern closely mirrors REST API resource management

---

### 7. ISBN Validator

Validates both ISBN-10 and ISBN-13 codes using their respective checksum algorithms. Handles edge cases including the special `X` check digit for ISBN-10 and correct alternating-weight multiplication for ISBN-13.

**Key concepts:**
- Checksum algorithms
- Regular expression input sanitisation
- `enumerate` for index-aware iteration
- Multiple return paths with early exits

**Skills demonstrated:**
- Implementing real-world validation standards
- Separating validation logic from calculation logic
- Working with `re` for input sanitisation

**Technologies / libraries used:**
- `re`

---

### 8. Musical Instrument Inventory

Introduces object-oriented programming with a simple `MusicalInstrument` class. Demonstrates class instantiation, instance attributes, and defining instance methods that describe object behaviour.

**Key concepts:**
- Class definition with `__init__`
- Instance attributes and methods
- Object instantiation and method calls

**Skills demonstrated:**
- Modelling real-world entities as Python objects
- Writing classes with clear responsibilities
- Foundational OOP for larger systems

---

### 9. Planet Class

Defines a `Planet` class with strict validation in `__init__`, raising `TypeError` and `ValueError` for invalid inputs. Implements `__str__` for clean string representation and an `orbit()` method for descriptive behaviour.

**Key concepts:**
- Constructor validation with exceptions
- `__str__` dunder method
- `TypeError` and `ValueError`
- Clean class API design

**Skills demonstrated:**
- Writing robust, self-validating classes
- Overriding dunder methods for readable output
- Using exceptions to enforce invariants

---

### 10. Email Simulator

A multi-class email system modelling `User`, `Email`, and `Inbox` objects. Users can send emails, check their inbox, read messages (auto-marking them as read), and delete emails. Uses `datetime` for timestamp generation.

**Key concepts:**
- Multi-class OOP design
- Object composition (User has an Inbox, Inbox has Emails)
- `datetime` module for timestamps
- Read/unread state management

**Skills demonstrated:**
- Designing interconnected class systems
- Object composition over inheritance
- Building features that mirror real application logic

**Technologies / libraries used:**
- `datetime`

---

### 11. Budget App

A budget tracking application where spending categories maintain a transaction ledger. Supports deposits, withdrawals, transfers between categories, and generates an ASCII bar chart showing percentage spent per category.

**Key concepts:**
- Ledger-based financial tracking
- String formatting with `.ljust`, `.rjust`, and f-strings
- Percentage calculation and ASCII chart rendering
- Class `__str__` for formatted output

**Skills demonstrated:**
- Building a stateful, data-driven application
- Producing formatted reports from raw data
- Implementing real-world financial logic in OOP

---

### 12. Salary Tracker

An `Employee` class using Python `@property` decorators with custom getters and setters to enforce business rules: salary must exceed the base for the employee's level, levels cannot be downgraded, and promotion automatically updates salary.

**Key concepts:**
- `@property`, `@name.setter` decorators
- Private attributes with name-mangling convention
- `__str__` and `__repr__` dunder methods
- Class-level data with `_base_salaries`

**Skills demonstrated:**
- Encapsulation through controlled property access
- Enforcing business rules at the setter level
- Writing Pythonic, well-structured class APIs

---

### 13. Game Character

A `GameCharacter` class that uses `@property` setters to clamp health (0–100) and mana (0–50) values automatically. A `level_up()` method advances the level and resets stats to full.

**Key concepts:**
- Value clamping with property setters
- Private attributes and public read-only properties
- State mutation through methods

**Skills demonstrated:**
- Applying property setters for automatic value bounding
- Designing game-logic rules into class behaviour
- Producing clean `__str__` output for object state

---

### 14. Media Catalogue App

A catalogue application for `Movie` and `TVSeries` objects using class inheritance. Defines a custom `MediaError` exception. The catalogue filters by type using `type()` vs `isinstance()` comparisons and handles errors gracefully.

**Key concepts:**
- Class inheritance with `super().__init__()`
- Custom exception classes
- `type()` vs `isinstance()` distinction
- Polymorphic `__str__` output

**Skills demonstrated:**
- Designing inheritance hierarchies
- Creating domain-specific exceptions
- Building a collection class with type-aware filtering

---

### 15. Discount Calculator

Implements the **Strategy design pattern** using Python's Abstract Base Classes (`ABC`). Three interchangeable discount strategies (percentage, fixed amount, premium user) are evaluated by a `DiscountEngine` that selects the best price.

**Key concepts:**
- `ABC` and `@abstractmethod`
- Strategy design pattern
- Type hints (`List`, `->`)
- Polymorphic method dispatch

**Skills demonstrated:**
- Applying software design patterns in Python
- Writing extensible, open/closed-principle-friendly code
- Using abstract interfaces to enforce contracts

**Technologies / libraries used:**
- `abc`, `typing`

---

### 16. Player Interface

Defines an abstract `Player` base class with a concrete `make_move()` method and an abstract `level_up()` method. A `Pawn` subclass implements the interface and demonstrates random movement on a coordinate grid.

**Key concepts:**
- Abstract Base Classes with mixed concrete/abstract methods
- Coordinate-based movement simulation
- `random.choice` for non-deterministic behaviour
- Path tracking with a list

**Skills demonstrated:**
- Designing reusable abstract interfaces
- Separating shared behaviour from subclass-specific logic
- Using randomness in simulations

**Technologies / libraries used:**
- `abc`, `random`

---

### 17. Polygon Area Calculator

Implements `Rectangle` and `Square` classes using inheritance. `Square` overrides `set_width` and `set_height` to keep sides equal. Methods compute area, perimeter, diagonal, ASCII picture, and how many smaller shapes fit inside a larger one.

**Key concepts:**
- Inheritance and method overriding
- `math.sqrt` for geometric calculations
- ASCII art generation with string multiplication
- Integer division for fitting calculations

**Skills demonstrated:**
- Applying the Liskov Substitution Principle
- Building a clean geometric class hierarchy
- Generating visual output from computed values

**Technologies / libraries used:**
- `math`

---

### 18. Linked List

Implements a singly linked list from scratch with a nested `Node` class. Supports adding elements to the tail and removing elements by value, with correct pointer re-linking for all cases (head removal, mid-list removal).

**Key concepts:**
- Linked list data structure
- Nested class for node representation
- Pointer traversal and re-linking
- Edge case handling (empty list, head node)

**Skills demonstrated:**
- Building foundational data structures without built-in shortcuts
- Managing node references and pointer logic
- Understanding memory layout behind Python lists

---

### 19. Hash Table

Builds a custom hash table that converts string keys to integer hashes using character ordinal values. Handles hash collisions by chaining into nested dictionaries. Supports add, remove, and lookup operations.

**Key concepts:**
- Hash function implementation using `ord()`
- Collision handling via chaining
- Dictionary-backed storage

**Skills demonstrated:**
- Understanding how hash maps work under the hood
- Implementing collision resolution strategies
- Building core data structures from first principles

---

### 20. Binary Search

Implements the binary search algorithm on a sorted list. Tracks the search path (all midpoint values visited) and returns both the path and the final index on a successful search.

**Key concepts:**
- Binary search algorithm
- Low/high pointer manipulation
- Path tracking during search
- O(log n) time complexity

**Skills demonstrated:**
- Implementing efficient search algorithms
- Reasoning about sorted data structures
- Returning rich diagnostic information from algorithms

---

### 21. Bisection Method — Square Root Approximation

Uses the bisection (interval halving) method as a numerical technique to approximate square roots to a configurable tolerance. Demonstrates iterative convergence and handling of edge cases (0, 1, negative numbers).

**Key concepts:**
- Bisection / interval halving algorithm
- Numerical methods and convergence
- Tolerance-based iteration with a max iteration cap
- Edge case handling for mathematical constraints

**Skills demonstrated:**
- Applying mathematical algorithms in code
- Building configurable, convergence-based functions
- Handling floating-point precision

---

### 22. Merge Sort

Implements the merge sort algorithm using a divide-and-conquer approach. Recursively splits an array in half, sorts each half, then merges them back in sorted order.

**Key concepts:**
- Merge sort algorithm
- Divide and conquer
- Recursion with base case
- O(n log n) time complexity

**Skills demonstrated:**
- Writing clean recursive algorithms
- Understanding divide-and-conquer strategy
- Implementing a stable, efficient sorting algorithm

---

### 23. Quick Sort

Implements quick sort using a pivot-based partitioning approach. Separates elements into `less`, `equal`, and `greater` sublists relative to the pivot and recursively sorts each partition.

**Key concepts:**
- Quick sort algorithm
- Pivot selection and three-way partitioning
- Recursion
- O(n log n) average / O(n²) worst case

**Skills demonstrated:**
- Applying in-place (conceptual) sorting logic
- Understanding partitioning strategies
- Comparing trade-offs between sorting algorithms

---

### 24. Selection Sort

Implements the selection sort algorithm by repeatedly finding the minimum element in the unsorted portion of the array and swapping it into position.

**Key concepts:**
- Selection sort algorithm
- Nested loop traversal
- In-place swapping with tuple unpacking
- O(n²) time complexity

**Skills demonstrated:**
- Understanding simple sorting algorithms
- Performing in-place array manipulation
- Reasoning about algorithmic complexity

---

### 25. Luhn Algorithm — Credit Card Validator

Validates credit card numbers using the Luhn algorithm. Reverses the digit string, doubles every second digit, subtracts 9 from results over 9, sums all digits, and checks divisibility by 10.

**Key concepts:**
- Luhn checksum algorithm
- String reversal and character iteration
- Modular arithmetic
- Real-world payment validation standard

**Skills demonstrated:**
- Implementing industry-standard validation logic
- Working with digit-level string manipulation
- Applying mathematical rules to real-world data

---

### 26. Tower of Hanoi

Solves the Tower of Hanoi puzzle recursively for n disks. Tracks the state of all three rods after each move and returns the complete move sequence as a formatted string.

**Key concepts:**
- Tower of Hanoi recursive algorithm
- Three-rod state management with lists
- Recursive decomposition
- Move logging and state snapshots

**Skills demonstrated:**
- Translating recursive mathematical logic into code
- Managing mutable state across recursive calls
- Visualising algorithm execution step by step

---

## 🛠 Technologies

- Python 3
- Git & GitHub
- Standard library: `re`, `datetime`, `abc`, `typing`, `math`, `random`

---

## 🚀 Learning Outcome

This repository demonstrates practical Python engineering skills built through deliberate, project-based practice. The progression — from core syntax through OOP, custom data structures, design patterns, and algorithm implementation — directly maps to the competencies required for professional backend development.

| Framework / Tool | How this repo prepares you |
|---|---|
| **Django** | Class-based design, model validation, ORM patterns, encapsulation |
| **Django REST Framework** | Serializer validation logic, viewset patterns, permission enforcement |
| **API Design** | Request validation, business rule separation, structured error handling |
| **Code Quality** | Clean architecture, defensive programming, single-responsibility functions |

---

## 🔗 Related Repositories

**JavaScript Projects**
[github.com/sadykovIsmail/Java-script](https://github.com/sadykovIsmail/Java-script)

**React Frontend Projects**
[github.com/sadykovIsmail/frontend-projects-collection](https://github.com/sadykovIsmail/frontend-projects-collection)

**Django Backend APIs**
[github.com/sadykovIsmail/django_advanced_rest_api_course](https://github.com/sadykovIsmail/django_advanced_rest_api_course)

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).
