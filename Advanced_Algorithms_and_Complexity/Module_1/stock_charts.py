# python3

def read_data():
    n, m = map(int, input().split())
    return [list(map(int, input().split())) for _ in range(n)]

def is_strictly_less(a, b):
    return all(x < y for x, y in zip(a, b))

def build_graph(stock_data):
    n = len(stock_data)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and is_strictly_less(stock_data[i], stock_data[j]):
                graph[i].append(j)
    return graph

def bpm(u, graph, visited, match_to):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if match_to[v] == -1 or bpm(match_to[v], graph, visited, match_to):
                match_to[v] = u
                return True
    return False

def min_charts(stock_data):
    graph = build_graph(stock_data)
    n = len(stock_data)
    match_to = [-1] * n
    result = 0
    for u in range(n):
        visited = [False] * n
        if bpm(u, graph, visited, match_to):
            result += 1
    return n - result

def main():
    stock_data = read_data()
    print(min_charts(stock_data))

if __name__ == "__main__":
    main()
