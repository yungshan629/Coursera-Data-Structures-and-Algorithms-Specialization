from typing import List

def explore(v: int, adj: List[List[int]], visited: List[bool]):
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(w, adj, visited)

def reach(adj: List[List[int]], x: int, y: int) -> int:
    visited = [False] * len(adj)
    explore(x, adj, visited)
    return 1 if visited[y] else 0

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        a, b = x - 1, y - 1
        adj[a].append(b)
        adj[b].append(a)
    x, y = map(int, input().split())
    print(reach(adj, x - 1, y - 1))

if __name__ == "__main__":
    main()
