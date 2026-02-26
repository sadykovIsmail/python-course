![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Projects](https://img.shields.io/badge/Projects-26%20Exercises-22c55e?style=flat)
![OOP](https://img.shields.io/badge/OOP-Classes%20%7C%20Inheritance%20%7C%20Patterns-8b5cf6?style=flat)
![Algorithms](https://img.shields.io/badge/Algorithms-Search%20%7C%20Sort%20%7C%20Recursion-f59e0b?style=flat)

# 🛠 Professional Projects

A progressive series of 26 applied Python exercises ranging from beginner scripts to object-oriented systems, design patterns, and algorithm implementations. Each project tackles a real engineering problem and is written with production habits: input validation, encapsulation, clear error handling, and modular structure.

---

## 📋 Project Index

| # | Project | Key Concept | Difficulty |
|---|---|---|---|
| 0 | [Hello World](#0-hello-world) | Functions & modules | ⭐ |
| 1 | [Caesar Cipher](#1-caesar-cipher) | String manipulation, `str.maketrans` | ⭐⭐ |
| 2 | [RPG Character Creator](#2-rpg-character-creator) | Input validation, f-strings | ⭐⭐ |
| 3 | [PIN Extractor](#3-pin-extractor) | Nested loops, text parsing | ⭐⭐ |
| 4 | [Number Pattern Generator](#4-number-pattern-generator) | Loops, generator expressions | ⭐ |
| 5 | [Medical Data Validation](#5-medical-data-validation) | Regex, dict validation | ⭐⭐⭐ |
| 6 | [User Configuration Manager](#6-user-configuration-manager) | Dictionary CRUD | ⭐⭐ |
| 7 | [ISBN Validator](#7-isbn-validator) | Checksum algorithms, regex | ⭐⭐⭐ |
| 8 | [Musical Instrument Inventory](#8-musical-instrument-inventory) | OOP basics | ⭐⭐ |
| 9 | [Planet Class](#9-planet-class) | OOP, dunder methods, validation | ⭐⭐ |
| 10 | [Email Simulator](#10-email-simulator) | Multi-class OOP, `datetime` | ⭐⭐⭐ |
| 11 | [Budget App](#11-budget-app) | OOP, ledger system, ASCII chart | ⭐⭐⭐ |
| 12 | [Salary Tracker](#12-salary-tracker) | `@property`, business rules | ⭐⭐⭐ |
| 13 | [Game Character](#13-game-character) | Property setters, value clamping | ⭐⭐⭐ |
| 14 | [Media Catalogue App](#14-media-catalogue-app) | Inheritance, custom exceptions | ⭐⭐⭐ |
| 15 | [Discount Calculator](#15-discount-calculator) | Strategy pattern, ABC | ⭐⭐⭐⭐ |
| 16 | [Player Interface](#16-player-interface) | Abstract base class, `random` | ⭐⭐⭐ |
| 17 | [Polygon Area Calculator](#17-polygon-area-calculator) | Inheritance, `math`, LSP | ⭐⭐⭐ |
| 18 | [Linked List](#18-linked-list) | Data structure from scratch | ⭐⭐⭐ |
| 19 | [Hash Table](#19-hash-table) | Hash function, collision chaining | ⭐⭐⭐⭐ |
| 20 | [Binary Search](#20-binary-search) | O(log n) search algorithm | ⭐⭐⭐ |
| 21 | [Bisection Method](#21-bisection-method) | Numerical methods, convergence | ⭐⭐⭐ |
| 22 | [Merge Sort](#22-merge-sort) | Divide-and-conquer, O(n log n) | ⭐⭐⭐ |
| 23 | [Quick Sort](#23-quick-sort) | Pivot partitioning, recursion | ⭐⭐⭐ |
| 24 | [Selection Sort](#24-selection-sort) | In-place sorting, O(n²) | ⭐⭐ |
| 25a | [Luhn Algorithm](#25a-luhn-algorithm) | Checksum validation, real-world standard | ⭐⭐⭐ |
| 25b | [Tower of Hanoi](#25b-tower-of-hanoi) | Recursion, state tracking | ⭐⭐⭐⭐ |

---

## Project Details

---

### 0. Hello World

**File:** `0.hello world.py`

The entry point of the repository. Defines two functions: `hello()` returns a greeting string, and `hi()` calls `hello()` and extends it. Demonstrates basic function composition.

**Concepts:** function definition, return values, string concatenation, calling functions from other functions.

---

### 1. Caesar Cipher

**File:** `1. caesar_clipher.py`

Encrypts and decrypts text using the Caesar cipher — one of the oldest substitution ciphers. Each letter is shifted by a configurable amount. Uses `str.maketrans` and `str.translate` for efficient, O(n) character-level mapping.

**Concepts:** `str.maketrans`, `str.translate`, input validation (type and range), optional `encrypt` parameter, alphabet manipulation.

**Key features:**
- Supports both encryption (`encrypt=True`) and decryption (`encrypt=False`)
- Validates that the shift is an integer between 1 and 25
- Preserves case using upper and lower alphabet variants in the translation table

**Example:**
```python
caesar('freeCodeCamp', 3)    # → 'iuhhFrghFdps'
caesar('iuhhFrghFdps', 3, encrypt=False)  # → 'freeCodeCamp'
```

---

### 2. RPG Character Creator

**File:** `2. rpg character.py`

Creates an RPG character sheet with three stats (strength, intelligence, charisma) that must sum to exactly 7. Renders the result as a formatted visual output using dot characters.

**Concepts:** multi-condition input validation, `isinstance`, `all()`, f-strings, visual string construction.

**Key features:**
- Rejects names that are too long, contain spaces, or are not strings
- Ensures all stats are integers between 1 and 4 and sum to 7
- Renders filled (`●`) and empty (`○`) dots for each stat

**Example:**
```python
create_character("Hero", 3, 2, 2)
# → Hero
#   STR ●●●○○○○○○○
#   INT ●●○○○○○○○○
#   CHA ●●○○○○○○○○
```

---

### 3. PIN Extractor

**File:** `3. pin extractor.py`

Extracts hidden numerical codes from poems. For each line, reads the length of the word at the position matching the line index. If no word exists at that position, contributes `'0'` to the code.

**Concepts:** `str.split`, `enumerate`, nested iteration, list building, edge case handling.

**Key features:**
- Processes multiple poems in a single call
- Handles lines with fewer words than the line index
- Returns a list of extracted codes, one per poem

---

### 4. Number Pattern Generator

**File:** `4. numbet pattern generator.py`

Generates a space-separated string of integers from 1 to n. Includes both an explicit loop implementation and a concise generator-expression version in a comment for comparison.

**Concepts:** `str.join`, generator expressions, loop-based string building, input validation.

**Example:**
```python
number_pattern(4)  # → '1 2 3 4'
```

---

### 5. Medical Data Validation

**File:** `5. medical data validation.py`

Validates a list of patient medical records against strict format rules. Checks every field of every record and reports exactly which fields fail and at which position in the list.

**Concepts:** `re.fullmatch`, `re.IGNORECASE`, dictionary key-set validation, `isinstance` with nested types, structured error reporting.

**Key features:**
- Validates patient IDs against pattern `P\d+` (case-insensitive)
- Validates visit IDs against pattern `V\d+` (case-insensitive)
- Checks age is an integer ≥ 18
- Confirms medications is a list of strings
- Reports invalid fields by name and position

**Technologies:** `re`

---

### 6. User Configuration Manager

**File:** `6.user configuration manager.py`

Implements CRUD operations for a key-value settings dictionary. Normalises all keys and values to lowercase. Prevents duplicate keys on add and reports clearly when an update targets a non-existent key.

**Concepts:** dictionary operations (`update`, `pop`, iteration), lowercase normalisation, multi-line f-string output.

**Key features:**
- `add_setting` — adds a new entry; rejects duplicates
- `update_setting` — updates an existing entry; rejects unknown keys
- `delete_setting` — removes an entry by key
- `view_settings` — formats all entries for display

---

### 7. ISBN Validator

**File:** `7. isbn validator.py`

Validates ISBN-10 and ISBN-13 codes by computing and comparing the standard checksum digit. Accepts user input as a comma-separated pair of `isbn, length` and provides clear error messages for every invalid input pattern.

**Concepts:** checksum algorithm, alternating-weight multiplication (ISBN-13), modular arithmetic, `re.fullmatch`, `enumerate`.

**Key features:**
- ISBN-10: weighted sum divided by 11, handles `X` check digit
- ISBN-13: alternating ×1 / ×3 weights, result mod 10
- Validates length, digit characters, and format before computing

**Technologies:** `re`

---

### 8. Musical Instrument Inventory

**File:** `8.musical instriment inventory.py`

Defines a `MusicalInstrument` class with `name` and `instrument_type` attributes and two instance methods. A clean, minimal introduction to class-based object modelling.

**Concepts:** class definition, `__init__`, instance attributes, instance methods.

**Example:**
```python
instrument = MusicalInstrument('Oboe', 'woodwind')
instrument.play()      # → The Oboe is fun to play!
instrument.get_fact()  # → The Oboe is part of the woodwind family of instruments.
```

---

### 9. Planet Class

**File:** `9.planet class.py`

A `Planet` class with constructor-level validation using `TypeError` and `ValueError`. Implements `__str__` for clean string output and an `orbit()` method for descriptive behaviour.

**Concepts:** `__init__` validation, `isinstance`, empty string checks, `__str__` dunder method, instance methods.

**Example:**
```python
p = Planet("Earth", "terrestrial", "Sun")
str(p)       # → 'Planet: Earth | Type: terrestrial | Star: Sun'
p.orbit()    # → 'Earth is orbiting around Sun...'
```

---

### 10. Email Simulator

**File:** `10. email simulator.py`

A three-class system modelling `User`, `Email`, and `Inbox`. Users send emails to each other, each email is timestamped with `datetime.now()`, and the inbox supports listing, reading (auto-marks as read), and deleting emails.

**Concepts:** object composition, multi-class design, `datetime`, read/unread state, index-based list access with bounds checking.

**Key features:**
- `Email.mark_as_read()` called automatically on `display_full_email()`
- `Inbox` validates index bounds before any read or delete operation
- `User.send_email()` creates the Email and delivers it to the receiver's inbox

**Technologies:** `datetime`

---

### 11. Budget App

**File:** `11. budget app.py`

A full budget tracking application. Each `Category` maintains a transaction ledger and supports deposits, withdrawals, and transfers. The `create_spend_chart` function generates an ASCII bar chart showing percentage withdrawn per category.

**Concepts:** list of dicts for ledger, `__str__` with `.ljust`/`.rjust`, percentage calculation, ASCII chart construction.

**Key features:**
- `check_funds` prevents overdraft on withdraw and transfer
- `__str__` formats the ledger as a 30-character wide receipt
- `create_spend_chart` renders a percentage bar chart (0–100 in steps of 10)

**Example output:**
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant               -15.89
Total: 973.96
```

---

### 12. Salary Tracker

**File:** `12. salary tracker.py`

An `Employee` class that uses `@property` with custom setters to enforce business rules. Salary cannot be set below the level's base rate. Level can only be promoted (not downgraded). Promotion automatically adjusts salary.

**Concepts:** `@property`, `@x.setter`, `_private` attributes, `__str__` and `__repr__`, class-level dictionary for base salaries, `TypeError`/`ValueError`.

**Key features:**
- Three separately validated properties: `name`, `level`, `salary`
- Level setter enforces forward-only progression through trainee → junior → mid-level → senior
- Salary setter rejects values at or below the level's base salary

---

### 13. Game Character

**File:** `13. game character.py`

A `GameCharacter` class with health (0–100) and mana (0–50) properties that automatically clamp any assigned value to their valid range. `level_up()` increments the level and resets both stats to full.

**Concepts:** `@property` setters with clamping logic, private attributes, read-only `name` property, `__str__`.

**Example:**
```python
hero = GameCharacter("Ismail")
hero.health = 150   # clamped to 100
hero.mana = -10     # clamped to 0
hero.level_up()     # level 2, health=100, mana=50
```

---

### 14. Media Catalogue App

**File:** `14. media catalogue app.py`

A media catalogue that holds `Movie` and `TVSeries` objects. `TVSeries` extends `Movie` via inheritance. A custom `MediaError` exception rejects non-Movie objects. The catalogue separates movies from series using `type()` vs `isinstance()`.

**Concepts:** inheritance with `super().__init__()`, custom exception with object reference, `type()` for exact match, `isinstance()` for subclass inclusion, try/except in user code.

**Key features:**
- `MediaError` carries the offending object as `.obj` for detailed error reporting
- `get_movies()` uses `type(item) is Movie` to exclude TVSeries instances
- `get_tv_series()` uses `isinstance` to include all TVSeries subclasses

---

### 15. Discount Calculator

**File:** `15. discount calculator.py`

Implements the **Strategy design pattern** via Python's ABC. Three discount strategies (`PercentageDiscount`, `FixedAmountDiscount`, `PremiumUserDiscount`) each implement `is_applicable()` and `apply_discount()`. A `DiscountEngine` evaluates all applicable strategies and returns the best (lowest) price.

**Concepts:** `ABC`, `@abstractmethod`, Strategy pattern, type hints (`List`, `->` return annotations), polymorphism.

**Key features:**
- Strategies are fully interchangeable — new ones can be added without touching `DiscountEngine`
- Engine calculates all applicable prices and picks the minimum
- Type annotations document the expected interface throughout

**Technologies:** `abc`, `typing`

---

### 16. Player Interface

**File:** `16. Player interface.py`

Defines an abstract `Player` base class with a shared `make_move()` implementation and an abstract `level_up()` contract. The concrete `Pawn` subclass defines its available moves and extends them on level-up. Movement is randomised using `random.choice`.

**Concepts:** `ABC`, mixed concrete/abstract methods, coordinate grid, `random.choice`, path tracking.

**Technologies:** `abc`, `random`

---

### 17. Polygon Area Calculator

**File:** `17.polygon area calculator.py`

A `Rectangle` class with geometric methods, extended by a `Square` subclass that enforces equal width and height through overridden setters. Demonstrates the Liskov Substitution Principle: a `Square` can be used anywhere a `Rectangle` is expected.

**Concepts:** inheritance, method overriding, `math.sqrt`, ASCII picture rendering, integer division for shape fitting.

**Key features:**
- `get_area()`, `get_perimeter()`, `get_diagonal()`, `get_picture()`, `get_amount_inside()`
- `Square.set_side()` keeps width and height in sync
- `Square` overrides `set_width` and `set_height` to delegate to `set_side`

**Technologies:** `math`

---

### 18. Linked List

**File:** `18. linked list.py`

Implements a singly linked list from scratch. `Node` is a nested class holding an `element` and a `next` pointer. `add()` appends to the tail; `remove()` re-links pointers correctly for head removal, mid-list removal, and not-found cases.

**Concepts:** singly linked list, nested class, pointer traversal, head/tail edge cases.

**Key operations:**
- `add(element)` — O(n) tail append
- `remove(element)` — O(n) search and re-link
- `is_empty()` — O(1) length check

---

### 19. Hash Table

**File:** `19. hash table.py`

A custom hash table backed by a Python dictionary. The `hash()` method sums character ordinals for string keys (or passes numeric keys through). Collisions are resolved by chaining — keys that hash to the same bucket are stored in a nested dictionary at that bucket.

**Concepts:** hash function design, `ord()`, collision resolution via chaining, dictionary-within-dictionary storage.

**Key operations:**
- `add(key, value)` — computes hash, creates or extends the bucket
- `remove(key)` — removes the key from its bucket
- `lookup(key)` — retrieves a value by key

---

### 20. Binary Search

**File:** `20. binary search.py`

A clean implementation of binary search with path tracking. Returns both the sequence of midpoint values examined and the final index on success, or a not-found message on failure.

**Concepts:** binary search, low/high pointer manipulation, O(log n) time complexity.

**Example:**
```python
binary_search([1, 2, 3, 4, 5], 3)
# → ([1, 3], 'Value found at index 2')

binary_search([1, 3, 5, 9, 14, 22], 10)
# → 'Value not found'
```

---

### 21. Bisection Method

**File:** `21. bisection method.py`

Uses the bisection (interval halving) method to approximate the square root of a number to a configurable tolerance. Iterates until `|mid² - number| <= tolerance` or the maximum iteration count is reached.

**Concepts:** bisection algorithm, floating-point convergence, `abs()`, max iteration guard, edge cases for 0, 1, and negative inputs.

**Example:**
```python
square_root_bisection(16)   # → 4.0
square_root_bisection(2)    # → ≈ 1.4142135...
square_root_bisection(-1)   # → raises ValueError
```

---

### 22. Merge Sort

**File:** `22. merge sort.py`

A clean, two-function implementation of merge sort. `merge_sort` recursively splits the array at the midpoint. `merge` combines two sorted halves into a single sorted list using two-pointer traversal.

**Concepts:** divide and conquer, recursion, stable sort, O(n log n) time complexity.

**Example:**
```python
merge_sort([5, 2, 8, 1, 9])  # → [1, 2, 5, 8, 9]
```

---

### 23. Quick Sort

**File:** `23. quick sort.py`

Three-way partitioning quick sort. The pivot is always the first element. Elements are partitioned into `less`, `equal`, and `greater` lists, then the `less` and `greater` partitions are recursively sorted.

**Concepts:** pivot selection, three-way partitioning, recursion, O(n log n) average / O(n²) worst case.

**Example:**
```python
quick_sort([3, 6, 8, 10, 1, 2, 1])  # → [1, 1, 2, 3, 6, 8, 10]
```

---

### 24. Selection Sort

**File:** `24. selection sort.py`

Selection sort finds the minimum element in the unsorted portion of the array and swaps it into position. Continues until the array is fully sorted. Uses Python's tuple-unpacking swap.

**Concepts:** nested loops, minimum tracking, in-place swap, O(n²) time complexity.

**Example:**
```python
selection_sort([64, 25, 12, 22, 11])  # → [11, 12, 22, 25, 64]
```

---

### 25a. Luhn Algorithm

**File:** `25. Luhn algorithm.py`

Validates credit card numbers using the Luhn algorithm — the same standard used by payment processors worldwide. Strips spaces and dashes, reverses the digits, doubles every second digit (subtracting 9 if > 9), sums all digits, and checks if the total is divisible by 10.

**Concepts:** Luhn checksum, string reversal, modular arithmetic, digit-level iteration.

**Example:**
```python
verify_card_number('4111 1111 1111 1111')  # → 'VALID!'
verify_card_number('1234 5678 9012 3456')  # → 'INVALID!'
```

---

### 25b. Tower of Hanoi

**File:** `25. tower of hanoi.py`

Solves the Tower of Hanoi puzzle recursively for any number of disks. Tracks the state of all three rods after every move and returns the full move log as a formatted string.

**Concepts:** Tower of Hanoi algorithm, recursion, mutable state across recursive calls, move logging.

**Example (3 disks):**
```
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

---

## 🛠 Technologies

- Python 3
- Standard library: `re`, `datetime`, `abc`, `typing`, `math`, `random`

---

## 🔗 Back to Main Repository

[← Return to main README](../../README.md)
