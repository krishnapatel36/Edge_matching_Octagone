import pulp

# Define the octagons data with minimal rotations
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

edges = ['top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'left', 'top-left']
nrows, ncols = 3, 3
noctagons = len(octagons)

# Define the optimization model
model = pulp.LpProblem("OctagonPuzzleWithNumbers", pulp.LpMinimize)

# Define variables
x = pulp.LpVariable.dicts("x", (range(nrows), range(ncols), range(noctagons), range(8)), cat='Binary')
y = pulp.LpVariable.dicts("y", (range(nrows), range(ncols), edges), lowBound=0, upBound=9, cat='Integer')

# Each octagon is assigned to one cell
for k in range(noctagons):
    model += pulp.lpSum(x[i][j][k][r] for i in range(nrows) for j in range(ncols) for r in range(8)) == 1

# Each cell is occupied by one octagon
for i in range(nrows):
    for j in range(ncols):
        model += pulp.lpSum(x[i][j][k][r] for k in range(noctagons) for r in range(8)) == 1

# Linking x and y
for i in range(nrows):
    for j in range(ncols):
        for e in edges:
            model += y[i][j][e] == pulp.lpSum(
                x[i][j][k][r] * octagons[k][(edges.index(e) - r) % 8]
                for k in range(noctagons) for r in range(8)
            )

# Shared edges must have the same number
for i in range(nrows):
    for j in range(ncols - 1):
        model += y[i][j]['right'] == y[i][j + 1]['left']

for i in range(nrows - 1):
    for j in range(ncols):
        model += y[i][j]['bottom'] == y[i + 1][j]['top']

# Dummy objective
model += 0

# Solve the model and store solutions
solutions = []

def store_solution():
    solution = {}
    for i in range(nrows):
        for j in range(ncols):
            for k in range(noctagons):
                for r in range(8):
                    if pulp.value(x[i][j][k][r]) == 1:
                        solution[(i, j)] = (k, r)
    solutions.append(solution)

# Solve and add no-good cuts
for _ in range(1):  # Adjust the range for more solutions
    model.solve(pulp.PULP_CBC_CMD())
    if pulp.LpStatus[model.status] != 'Optimal':
        break
    store_solution()
    model += pulp.lpSum(
        x[i][j][k][r] * int((i, j) in solutions[-1] and solutions[-1][(i, j)] == (k, r))
        for i in range(nrows) for j in range(ncols) for k in range(noctagons) for r in range(8)
    ) <= nrows * ncols - 1

# Print the solutions
for idx, solution in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    for (i, j), (k, r) in solution.items():
        numbers = [octagons[k][(edges.index(e) - r) % 8] for e in edges]
        print(f"At position ({i}, {j}): Numbers = {numbers}")

    print("")

