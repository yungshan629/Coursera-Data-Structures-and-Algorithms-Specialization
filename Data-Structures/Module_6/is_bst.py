class Node:
    def __init__(self, key=0, left=-1, right=-1):
        self.key = key
        self.left = left
        self.right = right

def isBSTUtil(tree, node_index, min_key, max_key):
    if node_index == -1:
        return True

    if tree[node_index].key < min_key or tree[node_index].key > max_key:
        return False

    return (isBSTUtil(tree, tree[node_index].left, min_key, tree[node_index].key) and
            isBSTUtil(tree, tree[node_index].right, tree[node_index].key, max_key))

def isBinarySearchTree(tree):
    if len(tree) == 0:
        return True

    return isBSTUtil(tree, 0, float('-inf'), float('inf'))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    nodes = int(data[0])
    tree = []
    index = 1
    for _ in range(nodes):
        key = int(data[index])
        left = int(data[index + 1])
        right = int(data[index + 2])
        tree.append(Node(key, left, right))
        index += 3

    if isBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

if __name__ == "__main__":
    main()
