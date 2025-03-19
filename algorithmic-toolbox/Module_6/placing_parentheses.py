import sys

def eval_expr(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        raise ValueError("Invalid operator")

def get_maximum_value(expression):
    n = (len(expression) + 1) // 2
    solution = [[(0, 0) for _ in range(n)] for _ in range(n)]
    
    digits = lambda i: int(expression[2 * i])
    op = lambda i: expression[2 * i + 1]
    
    for i in range(n):
        solution[i][i] = (digits(i), digits(i))
    
    for i in range(1, n):
        for j in range(i, n):
            temp_min = sys.maxsize
            temp_max = -sys.maxsize
            for k in range(j - i, j):
                a = eval_expr(solution[j - i][k][0], solution[k + 1][j][0], op(k))
                b = eval_expr(solution[j - i][k][1], solution[k + 1][j][1], op(k))
                c = eval_expr(solution[j - i][k][0], solution[k + 1][j][1], op(k))
                d = eval_expr(solution[j - i][k][1], solution[k + 1][j][0], op(k))
                temp_min = min(temp_min, a, b, c, d)
                temp_max = max(temp_max, a, b, c, d)
                solution[j - i][j] = (temp_min, temp_max)
    
    return solution[0][n - 1][1]

if __name__ == "__main__":
    expression = input().strip()
    print(get_maximum_value(expression))
