# PuzzleSolver

## Project Description
PuzzleSolver is a Python library and command-line tool that implements state-space search algorithms to solve the 8-puzzle (sliding tile puzzle). It supports various strategies:
- Random Search
- Breadth-First Search (BFS)
- Depth-First Search (DFS) with configurable depth limits
- Greedy Best-First Search with heuristic functions
- A* Search with heuristic functions

The project also provides performance analysis (moves required, number of states tested, execution time) over sets of puzzles with varying difficulty.

## Installation
### Prerequisites
- Python 3.6 or higher

### Clone the repository
```bash
git clone https://github.com/<username>/PuzzleSolver.git
cd PuzzleSolver
```

No external dependencies are required.

## Usage
### Solve a single puzzle interactively
```bash
python3 eight_puzzle.py
```
Follow the prompts to enter the initial board configuration (a string of digits), choose an algorithm, and (if applicable) a heuristic or depth limit.

### Run batch experiments
```bash
python3 eight_puzzle.py
```
This processes the provided `*_moves.txt` files in parallel and outputs performance results for each algorithm and heuristic.

### From Python
```python
from eight_puzzle import eight_puzzle
eight_puzzle("312045678", "A*", "h1")
```

## Features
- Board and State classes representing the 8-puzzle and search tree nodes
- Searcher framework with implementations:
  - Random Search
  - BFS and DFS (configurable depth limits)
  - Greedy Best-First Search (heuristics: `h1` (misplaced tiles), `h2` (Manhattan distance))
  - A* Search (heuristics: `h1`, `h2`)
- Timer class for measuring execution time
- Batch processing with multiprocessing
- Performance reporting (moves required, number of states tested)

### Documentation
For detailed API information, see the docstrings in `board.py`, `state.py`, `searcher.py`, and `timer.py`.
