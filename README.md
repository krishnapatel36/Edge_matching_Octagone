## Introduction

This project involves solving a puzzle where octagons with numbers on their edges must be arranged in a 3x3 grid. The arrangement must ensure that shared edges between adjacent octagons have the same number. Each octagon can be rotated to achieve the correct alignment.

## Octagons

Each octagon is defined by the numbers on its eight edges, in the following order: top, top-right, right, bottom-right, bottom, bottom-left, left, and top-left:

```python
octagons = [
    (1, 2, 4, 8, 7, 5, 3, 6),
    (7, 4, 3, 8, 5, 2, 6, 1),
    (6, 7, 8, 1, 2, 3, 4, 5),
    (6, 3, 1, 5, 2, 7, 8, 4),
    (7, 2, 4, 3, 8, 5, 6, 1),
    (7, 2, 6, 8, 5, 3, 1, 4),
    (5, 1, 4, 8, 3, 6, 2, 7),
    (2, 3, 5, 1, 4, 8, 6, 7),
    (6, 4, 7, 5, 1, 8, 2, 3)
]
```

## Grid Structure

The octagons are arranged in a 3x3 grid.

## Variables

### Decision Variables

- `x[i][j][k][r]`: A binary variable indicating whether octagon `k` with rotation `r` is placed at position `(i, j)`.
- `y[i][j][e]`: An integer variable indicating the number on edge `e` at position `(i, j)`.

### Constraints

1. **Assignment Constraint**: Each octagon is assigned to exactly one cell, and each cell contains exactly one octagon.

2. **Edge Number Matching**: Linking the decision variables `x` and `y` ensures that shared edges between adjacent octagons have the same number.

### Objective Function

A dummy objective function is used since the primary goal is to find feasible solutions that satisfy all constraints.

## Solving the Model

The model is solved using PuLP's CBC solver. After solving, multiple solutions are stored and printed.

## Output

The solution is printed, showing the octagon at each position and the numbers on its edges.

### Sample Output Format

```
Solution 1:
At position (0, 0): Numbers = [1, 2, 4, 8, 7, 5, 3, 6]
At position (0, 1): Numbers = [7, 4, 3, 8, 5, 2, 6, 1]
...
```

## Usage

1. **Dependencies**: Ensure you have PuLP installed.
   ```
   pip install pulp
   ```

2. **Run the Script**: Execute the script to solve the puzzle and print the solutions.
   ```
   python octagone_edge_matching_puzzle.py
   ```

3. **Modify Constraints**: Adjust the constraints if necessary to explore different arrangements or solutions.

## Conclusion

This project demonstrates the use of linear programming to solve a combinatorial puzzle, ensuring all constraints are met for a valid solution. The Octagon Puzzle with Numbers showcases how optimization techniques can be applied to puzzle-solving and other combinatorial problems.
