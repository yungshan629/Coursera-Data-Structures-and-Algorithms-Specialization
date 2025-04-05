# python3

def read_data():
    num_left, num_right = map(int, input().split())
    adj_matrix = [list(map(int, input().split())) for _ in range(num_left)]
    return adj_matrix

def bpm(u, adj_matrix, visited, match_to):
    for v, connected in enumerate(adj_matrix[u]):
        if connected and not visited[v]:
            visited[v] = True
            if match_to[v] == -1 or bpm(match_to[v], adj_matrix, visited, match_to):
                match_to[v] = u
                return True
    return False

def find_matching(adj_matrix):
    num_left = len(adj_matrix)
    num_right = len(adj_matrix[0])
    match_to = [-1] * num_right
    result = [-1] * num_left

    for u in range(num_left):
        visited = [False] * num_right
        if bpm(u, adj_matrix, visited, match_to):
            for v in range(num_right):
                if match_to[v] == u:
                    result[u] = v
                    break
    return result

def write_response(matching):
    print(" ".join(str(m + 1) if m != -1 else "-1" for m in matching))

def main():
    adj_matrix = read_data()
    matching = find_matching(adj_matrix)
    write_response(matching)

if __name__ == "__main__":
    main()
