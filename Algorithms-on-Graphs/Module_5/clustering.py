from dataclasses import dataclass
from math import hypot
from typing import List, Tuple

DEBUG = False

@dataclass
class Point2D:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x}, {self.y})"

class DisjointSets:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int):
        u_root = self.find(u)
        v_root = self.find(v)

        if u_root == v_root:
            return

        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[u_root] = v_root
            if self.rank[u_root] == self.rank[v_root]:
                self.rank[v_root] += 1

def distance(p1: Point2D, p2: Point2D) -> float:
    return hypot(p1.x - p2.x, p1.y - p2.y)

def clustering(points: List[Point2D], k: int) -> float:
    n = len(points)
    ds = DisjointSets(n)

    # 建立所有邊的列表
    edges = [
        (distance(points[i], points[j]), i, j)
        for i in range(n) for j in range(i + 1, n)
    ]

    edges.sort()

    num_clusters = n
    idx = 0

    while num_clusters >= k:
        dist, u, v = edges[idx]
        if DEBUG:
            print(f"{points[u]} -> {points[v]} : {dist:.2f}")
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            num_clusters -= 1
        idx += 1

    # 回退到合併前的那一條邊
    last_edge = edges[idx - 1]
    if DEBUG:
        print(f"Final edge: {points[last_edge[1]]} -> {points[last_edge[2]]}")
    return last_edge[0]

def main():
    n = int(input())
    points = [Point2D(*map(int, input().split())) for _ in range(n)]
    k = int(input())
    result = clustering(points, k)
    print(f"{result:.10f}")

if __name__ == "__main__":
    main()
