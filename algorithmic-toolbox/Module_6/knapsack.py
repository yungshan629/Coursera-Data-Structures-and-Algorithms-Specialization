def optimal_weight(W, w):
    n = len(w)
    values = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if j >= w[i - 1]:
                values[i][j] = max(w[i - 1] + values[i - 1][j - w[i - 1]],
                                   values[i - 1][j])
            else:
                values[i][j] = values[i - 1][j]
    
    return values[n][W]

if __name__ == "__main__":
    W, n = map(int, input().split())
    w = list(map(int, input().split()))
    print(optimal_weight(W, w))
