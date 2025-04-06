# python3

from fractions import Fraction

def allocate_ads(n, m, A, b, c):
    EPS = Fraction(1, 10**10)

    for i in range(n):
        if b[i] < 0:
            A[i] = [-x for x in A[i]]
            b[i] = -b[i]

    tableau = []
    for i in range(n):
        row = list(map(Fraction, A[i])) + \
              [Fraction(int(i == j)) for j in range(n)] + \
              [Fraction(int(i == j)) for j in range(n)] + \
              [Fraction(b[i])]
        tableau.append(row)

    phase1_obj = [Fraction(0)] * (m + n) + [Fraction(1)] * n + [Fraction(0)]
    tableau.append(phase1_obj)

    basis = [m + n + i for i in range(n)]

    def pivot(tableau, basis, row, col):
        pivot_val = tableau[row][col]
        tableau[row] = [x / pivot_val for x in tableau[row]]
        for i in range(len(tableau)):
            if i != row:
                factor = tableau[i][col]
                tableau[i] = [a - factor * b for a, b in zip(tableau[i], tableau[row])]
        basis[row] = col

    def simplex(tableau, basis, n_rows, n_cols, phase):
        while True:
            col = -1
            for j in range(n_cols):
                if tableau[-1][j] < -EPS:
                    col = j
                    break
            if col == -1:
                break  # Optimal

            row = -1
            for i in range(n_rows):
                if tableau[i][col] > EPS:
                    ratio = tableau[i][-1] / tableau[i][col]
                    if row == -1 or ratio < tableau[row][-1] / tableau[row][col]:
                        row = i
            if row == -1:
                return 1  # Unbounded
            pivot(tableau, basis, row, col)

        if phase == 1 and tableau[-1][-1] > EPS:
            return -1  # Infeasible
        return 0

    code = simplex(tableau, basis, n, m + 2 * n, phase=1)
    if code != 0:
        return code, []

    # Remove artificial variables
    for row in tableau:
        del row[m + n: m + 2 * n]
    del tableau[-1]

    tableau.append(list(map(lambda x: -Fraction(x), c)) + [Fraction(0)] * (n + 1))
    for i in range(n):
        var = basis[i]
        if var < m:
            coeff = -Fraction(c[var])
            for j in range(len(tableau[0])):
                tableau[-1][j] += coeff * tableau[i][j]

    code = simplex(tableau, basis, n, m + n, phase=2)
    if code != 0:
        return code, []

    result = [Fraction(0)] * (m + n)
    for i in range(n):
        if basis[i] < m:
            result[basis[i]] = tableau[i][-1]

    return 0, [float(result[i]) for i in range(m)]

# ----------------------------
def main():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    status, sol = allocate_ads(n, m, A, b, c)
    if status == -1:
        print("No solution")
    elif status == 1:
        print("Infinity")
    else:
        print("Bounded solution")
        print(' '.join('%.18f' % x for x in sol))

if __name__ == '__main__':
    main()
