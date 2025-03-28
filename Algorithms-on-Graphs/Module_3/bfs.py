from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

# 讀取邊資訊並建立無向圖
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

# 讀取起點與終點
start, end = map(int, input().split())
start -= 1
end -= 1

# BFS 計算最短距離
dist = [-1] * n
dist[start] = 0
q = deque([start])

while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if dist[neighbor] == -1:
            dist[neighbor] = dist[node] + 1
            q.append(neighbor)

print(dist[end])
