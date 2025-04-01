# Python3

def build_trie(patterns):
    trie = [{}]  # root is node 0
    for pattern in patterns:
        current = 0
        for char in pattern:
            if char in trie[current]:
                current = trie[current][char]
            else:
                trie.append({})
                trie[current][char] = len(trie) - 1
                current = trie[current][char]
    return trie

def main():
    n = int(input())
    patterns = [input().strip() for _ in range(n)]
    trie = build_trie(patterns)
    for i, node in enumerate(trie):
        for char in node:
            next_node = node[char]
            print("{}->{}:{}".format(i, next_node, char))

if __name__ == "__main__":
    main()
