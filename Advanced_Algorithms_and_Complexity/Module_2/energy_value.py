# python3

import sys
import numpy as np

EPS = 1e-6
PRECISION = 20

def read_equation():
    size = int(input())
    a = []
    b = []
    for _ in range(size):
        row = list(map(float, input().split()))
        a.append(row[:-1])
        b.append(row[-1])
    return np.array(a, dtype=float), np.array(b, dtype=float)

def select_pivot(a, used_rows, used_cols):
    n = len(a)
    for i in range(n):
        if not used_rows[i]:
            for j in range(n):
                if not used_cols[j] and abs(a[i][j]) > EPS:
                    return i, j
    raise ValueError("No valid pivot found")

def swap_rows(a, b, row1, row2):
    a[[row1, row2]] = a[[row2, row1]]
    b[[row1, row2]] = b[[row2, row1]]

def process_pivot(a, b, pivot_row, pivot_col):
    n = len(a)
    factor = a[pivot_row][pivot_col]
    a[pivot_row] /= factor
    b[pivot_row] /= factor

    for r in range(n):
        if r != pivot_row:
            multiplier = a[r][pivot_col]
            a[r] -= multiplier * a[pivot_row]
            b[r] -= multiplier * b[pivot_row]

def solve_equation(a, b):
    n = len(a)
    used_rows = [False] * n
    used_cols = [False] * n

    for _ in range(n):
        pivot_row, pivot_col = select_pivot(a, used_rows, used_cols)
        swap_rows(a, b, pivot_row, pivot_col)
        process_pivot(a, b, pivot_col, pivot_col)
        used_rows[pivot_col] = True
        used_cols[pivot_col] = True

    return b

def main():
    a, b = read_equation()
    solution = solve_equation(a, b)
    np.set_printoptions(precision=PRECISION, suppress=True)
    for val in solution:
        print(val)

if __name__ == '__main__':
    main()
