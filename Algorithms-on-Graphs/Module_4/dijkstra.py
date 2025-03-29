import heapq

def dijkstra(n, edges, start):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u - 1].append((v - 1, w))  # 將節點編號轉為 0-based

    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))

    return dist

# 主要執行區
def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    s, t = map(int, input().split())
    s -= 1
    t -= 1

    dist = dijkstra(n, edges, s)
    print(-1 if dist[t] == float('inf') else dist[t])

if __name__ == "__main__":
    main()
