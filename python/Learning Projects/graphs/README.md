![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Graph%20Data%20Structures-22c55e?style=flat)

# 🕸 Graphs — Data Structure Representations

A focused exercise comparing the two standard ways to represent a graph in memory: the **adjacency matrix** and the **adjacency list**. Uses the same four-node graph for both, making the trade-offs between the two representations immediately visible.

---

## Overview

Graphs model relationships between entities — users in a social network, pages on a website, nodes in a network. Before implementing graph algorithms (BFS, DFS, shortest path), you need to understand how to store the graph itself.

---

## Concepts Demonstrated

- Graph terminology: nodes (vertices) and edges
- Adjacency matrix — a 2D list where `matrix[i][j] = 1` means nodes `i` and `j` are connected
- Adjacency list — a list of lists where each entry holds the neighbours of that node
- Space complexity trade-offs between the two representations

---

## The Graph

The code models this undirected graph:

```
    A
   /|\
  B | D
   \|/
    (A connects to B, C, D)
    (B connects to A, D)
    (C connects to A)
    (D connects to A, B)
```

---

## How It Works

```python
# Adjacency matrix — O(V²) space
adjacency_matrix = [
    [0, 1, 1, 1],  # A connects to B, C, D
    [1, 0, 0, 1],  # B connects to A, D
    [1, 0, 0, 0],  # C connects to A only
    [1, 1, 0, 0],  # D connects to A, B
]

# Adjacency list — O(V + E) space
adjacency_list = [
    ['B', 'C', 'D'],  # Neighbours of A
    ['A', 'D'],       # Neighbours of B
    ['A'],            # Neighbours of C
    ['A', 'B'],       # Neighbours of D
]
```

---

## Comparison Table

| Property | Adjacency Matrix | Adjacency List |
|---|---|---|
| Space | O(V²) | O(V + E) |
| Check if edge exists | O(1) | O(degree) |
| Iterate all edges | O(V²) | O(V + E) |
| Best for | Dense graphs | Sparse graphs |

---

## Skills Demonstrated

- Modelling real-world relationships as graph data structures
- Choosing the appropriate representation based on graph density
- Reading and constructing 2D list-based data structures
- Foundation for implementing BFS and DFS traversal algorithms

---

## Technologies

- Python 3 (no external libraries)

---

## 🔗 Back

[← Learning Projects](../README.md) | [← Main README](../../../README.md)
