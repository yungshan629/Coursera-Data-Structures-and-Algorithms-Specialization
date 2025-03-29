from collections import deque

def bellman_ford(n, edges, start):
    INF = float('inf')
    dist = [INF] * n
    prev = [-1] * n
    dist[start] = 0
    prev[start] = start

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u

    neg_infty = set()
    in_queue = set()
    queue = deque()

    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            queue.append(v)
            in_queue.add(v)

    while queue:
        u = queue.popleft()
        neg_infty.add(u)
        for x, y, _ in edges:
            if x == u and y not in in_queue:
                queue.append(y)
                in_queue.add(y)

    return dist, prev, neg_infty

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u - 1, v - 1, w))  # <-- 轉為 0-based index

    s = int(input()) - 1  # <-- 起點也轉為 0-based index

    dist, prev, neg_infty = bellman_ford(n, edges, s)

    for v in range(n):
        if prev[v] == -1:
            print('*')
        elif v in neg_infty:
            print('-')
        else:
            print(dist[v])

if __name__ == '__main__':
    main()
