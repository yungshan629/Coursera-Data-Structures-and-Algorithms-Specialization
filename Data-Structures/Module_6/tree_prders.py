class TreeOrders:
    def __init__(self):
        self.n = 0
        self.key = []
        self.left = []
        self.right = []

    def read(self):
        import sys
        input = sys.stdin.read
        data = input().split()
        
        self.n = int(data[0])
        index = 1
        for _ in range(self.n):
            self.key.append(int(data[index]))
            self.left.append(int(data[index + 1]))
            self.right.append(int(data[index + 2]))
            index += 3

    def in_order(self):
        result = []
        stack = []
        current = 0
        while stack or current != -1:
            if current != -1:
                stack.append(current)
                current = self.left[current]
            else:
                current = stack.pop()
                result.append(self.key[current])
                current = self.right[current]
        return result

    def pre_order(self):
        result = []
        stack = [0]
        while stack:
            current = stack.pop()
            if current != -1:
                result.append(self.key[current])
                stack.append(self.right[current])
                stack.append(self.left[current])
        return result

    def post_order(self):
        result = []
        stack = []
        current = 0
        last_visited = -1
        while stack or current != -1:
            if current != -1:
                stack.append(current)
                current = self.left[current]
            else:
                peek = stack[-1]
                if self.right[peek] != -1 and last_visited != self.right[peek]:
                    current = self.right[peek]
                else:
                    result.append(self.key[peek])
                    last_visited = stack.pop()
        return result

def print_result(a):
    print(" ".join(map(str, a)))

def main_with_large_stack_space():
    import sys
    sys.setrecursionlimit(10**6)
    
    tree = TreeOrders()
    tree.read()
    
    print_result(tree.in_order())
    print_result(tree.pre_order())
    print_result(tree.post_order())

if __name__ == "__main__":
    main_with_large_stack_space()
