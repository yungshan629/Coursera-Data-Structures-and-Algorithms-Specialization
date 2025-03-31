def fibonacci_huge_naive(n, m):
    previous, current = 0, 1
    pisano = [0, 1]

    while True:
        previous, current = current, (previous + current) % m
        pisano.append(current)

        # Pisano 週期出現時：0, 1 重新出現
        if pisano[-2] == 0 and pisano[-1] == 1:
            pisano.pop()  # 移除最後的 1
            pisano.pop()  # 移除最後的 0
            break

    period_length = len(pisano)
    return pisano[n % period_length]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))