# python3

def build_trie(patterns):
    trie = [{}]  # 根節點為 0
    for pattern in patterns:
        current_node = 0
        for char in pattern:
            if char in trie[current_node]:
                current_node = trie[current_node][char]
            else:
                trie.append({})
                trie[current_node][char] = len(trie) - 1
                current_node = len(trie) - 1
    return trie

def trie_matching(text, patterns):
    trie = build_trie(patterns)
    positions = []

    for i in range(len(text)):
        node = 0
        j = i
        while j < len(text):
            c = text[j]
            if c in trie[node]:
                node = trie[node][c]
                j += 1
                if not trie[node]:  # 到達葉節點
                    positions.append(i)
                    break
            else:
                break
    return positions

# 主程式
if __name__ == "__main__":
    text = input().strip()
    n = int(input())
    patterns = [input().strip() for _ in range(n)]

    matches = trie_matching(text, patterns)
    print(" ".join(map(str, matches)))
