class Node:
    def __init__(self):
        self.key = None
        self.parent = None
        self.children = []

    def set_parent(self, parent):
        self.parent = parent
        parent.children.append(self)

def find_root(nodes):
    for node in nodes:
        if node.parent is None:
            return node

def branch_max_height(root):
    max_height = 0
    stack = [(root, 1)]
    
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        for child in node.children:
            stack.append((child, height + 1))
    
    return max_height

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    nodes = [Node() for _ in range(n)]
    
    for child_index in range(n):
        parent_index = int(data[child_index + 1])
        if parent_index >= 0:
            nodes[child_index].set_parent(nodes[parent_index])
        nodes[child_index].key = child_index
    
    root = find_root(nodes)
    max_height = branch_max_height(root)
    print(max_height)

if __name__ == "__main__":
    main()
