import pulp

# -------------------------------------------------------
# Data
# -------------------------------------------------------
villages = ["A", "B", "C", "D"]

population = {
    "A": 100,
    "B": 200,
    "C": 150,
    "D": 50
}

dist = {
    ("A","A"): 0, ("A","B"): 3, ("A","C"): 4, ("A","D"): 6,
    ("B","A"): 3, ("B","B"): 0, ("B","C"): 2, ("B","D"): 5,
    ("C","A"): 4, ("C","B"): 2, ("C","C"): 0, ("C","D"): 7,
    ("D","A"): 6, ("D","B"): 5, ("D","C"): 7, ("D","D"): 0
}

capacity = 250
num_libraries = 2

# -------------------------------------------------------
# MILP Model
# -------------------------------------------------------
model = pulp.LpProblem("Capacitated_Facility_Location", pulp.LpMinimize)

# Decision variables:
# y_j = 1 if library j is opened
y = pulp.LpVariable.dicts("y", villages, lowBound=0, upBound=1, cat="Binary")

# x_ij = 1 if village i assigned to library j
x = pulp.LpVariable.dicts("x",
                          (villages, villages),
                          lowBound=0, upBound=1,
                          cat="Binary")

# -------------------------------------------------------
# Objective: Minimize total (population-weighted) travel cost
# -------------------------------------------------------
model += pulp.lpSum(population[i] * dist[(i, j)] * x[i][j]
                    for i in villages for j in villages)

# -------------------------------------------------------
# Constraints
# -------------------------------------------------------

# (1) Exactly num_libraries open
model += pulp.lpSum(y[j] for j in villages) == num_libraries

# (2) Each demand node is assigned to exactly one library
for i in villages:
    model += pulp.lpSum(x[i][j] for j in villages) == 1

# (3) Assignment only allowed to open libraries
for i in villages:
    for j in villages:
        model += x[i][j] <= y[j]

# (4) Capacity constraint
for j in villages:
    model += pulp.lpSum(population[i] * x[i][j] for i in villages) <= capacity

# -------------------------------------------------------
# Solve
# -------------------------------------------------------
model.solve(pulp.PULP_CBC_CMD(msg=False))

# -------------------------------------------------------
# Output
# -------------------------------------------------------
print("Status:", pulp.LpStatus[model.status])
print("\nOpened libraries:")
for j in villages:
    if y[j].value() == 1:
        print("  Library at:", j)

print("\nAssignments:")
for i in villages:
    for j in villages:
        if x[i][j].value() == 1:
            print(f"  Village {i} -> Library {j}")

print("\nTotal Cost =", pulp.value(model.objective))
