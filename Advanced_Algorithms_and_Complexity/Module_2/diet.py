# python3

import sys
import itertools
from typing import List, Tuple

EPS = 1e-6
INF = 1e9

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    A = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
    b = list(map(float, sys.stdin.readline().split()))
    c = list(map(float, sys.stdin.readline().split()))
    return n, m, A, b, c

def is_feasible(sol: List[float], A: List[List[float]], b: List[float]) -> bool:
    for i in range(len(A)):
        if sum(A[i][j] * sol[j] for j in range(len(sol))) - b[i] > EPS:
            return False
    return True

def gaussian_elimination(A: List[List[float]], b: List[float]) -> Tuple[bool, List[float]]:
    n = len(A)
    m = len(A[0])
    aug = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(min(n, m)):
        pivot = i
        for j in range(i + 1, n):
            if abs(aug[j][i]) > abs(aug[pivot][i]):
                pivot = j
        if abs(aug[pivot][i]) < EPS:
            return False, []
        aug[i], aug[pivot] = aug[pivot], aug[i]
        for j in range(i + 1, n):
            factor = aug[j][i] / aug[i][i]
            for k in range(i, m + 1):
                aug[j][k] -= factor * aug[i][k]
    x = [0.0] * m
    for i in reversed(range(m)):
        rhs = aug[i][m]
        for j in range(i + 1, m):
            rhs -= aug[i][j] * x[j]
        if abs(aug[i][i]) < EPS:
            return False, []
        x[i] = rhs / aug[i][i]
    return True, x

def solve_diet_problem(n, m, A, b, c):
    # Add constraints: x_i >= 0 => -x_i <= 0
    for i in range(m):
        cons = [0.0] * m
        cons[i] = -1.0
        A.append(cons)
        b.append(0.0)

    # Add constraint to check boundedness: sum(x) <= INF
    A.append([1.0] * m)
    b.append(INF)

    solutions = []
    best_val = -float('inf')
    best_sol = []
    has_infinite = False

    for indices in itertools.combinations(range(len(A)), m):
        sub_A = [A[i] for i in indices]
        sub_b = [b[i] for i in indices]
        ok, sol = gaussian_elimination(sub_A, sub_b)
        if not ok:
            continue
        if any(x < -EPS for x in sol):
            continue
        if is_feasible(sol, A, b):
            val = sum(c[i] * sol[i] for i in range(m))
            if val > best_val + EPS:
                best_val = val
                best_sol = sol
                if sum(sol) > INF / 2:
                    has_infinite = True

    if not best_sol:
        print("No solution")
    elif has_infinite:
        print("Infinity")
    else:
        print("Bounded solution")
        print(" ".join('%.18f' % x for x in best_sol))

def main():
    n, m, A, b, c = read_input()
    solve_diet_problem(n, m, A, b, c)

if __name__ == '__main__':
    main()