class Rope:
    def __init__(self, s):
        self.s = s

    def process(self, i, j, k):
        # Replace this code with a faster implementation
        t = self.s[:i] + self.s[j + 1:]
        self.s = t[:k] + self.s[i:j + 1] + t[k:]

    def result(self):
        return self.s

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    s = data[0]
    rope = Rope(s)
    actions = int(data[1])
    index = 2
    for _ in range(actions):
        i = int(data[index])
        j = int(data[index + 1])
        k = int(data[index + 2])
        rope.process(i, j, k)
        index += 3
    
    print(rope.result())

if __name__ == "__main__":
    main()
