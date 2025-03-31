def fibonacci_sum(n):
    if n < 0:
        return 0
    if n <= 1:
        return n

    digit = [0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0] 
    return digit[n % 60]

def fibonacci_partial_sum(m, n):
    sum_n = fibonacci_sum(n)
    sum_m_minus_1 = fibonacci_sum(m - 1)
    return (sum_n - sum_m_minus_1 + 10) % 10

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum(m, n))


