# Find Path Project - Harvard's CS50x AI

This project is an implementation of Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms as part of the CS50x AI course at Harvard. It focuses on the foundational pathfinding techniques that drive search-based AI applications. Using both DFS and BFS, this project explores different ways of navigating a graph or grid to reach a goal state, illustrating how each algorithm handles decision trees, efficiency, and solution paths.

## Key Features

- **DFS**: A recursive, stack-based approach to explore nodes in-depth before backtracking.
- **BFS**: A queue-based algorithm for level-by-level exploration, ensuring the shortest path in unweighted scenarios.
- **Comparison and Analysis**: Highlights the strengths and limitations of each method in various scenarios.

Ideal for those studying pathfinding algorithms or seeking to understand the search foundations in AI.

## Project Structure

```sh
find_path/                      # Top-level package
├── __init__.py
├── main.py                     # Entry point of the application
├── inputs/                     # Handles different input methods
│   ├── __init__.py
│   ├── stdin.py
├── models/                     # Contains data models
│   ├── __init__.py
│   └── state.py                # Defines the State class
├── problems/                   # Sample problem instances
│   ├── __init__.py
│   └── sample_tree.py          # Creates an example tree
├── search/                     # Search algorithms and related classes
│   ├── __init__.py
│   ├── algorithm.py
│   ├── frontier.py
│   └── storage/                # Storage structures for search algorithms
│       ├── __init__.py
│       ├── abstract.py
│       ├── queue.py
│       └── stack.py
└── README.md
```
