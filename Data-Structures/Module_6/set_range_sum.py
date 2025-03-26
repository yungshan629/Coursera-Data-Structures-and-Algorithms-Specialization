class Vertex:
    def __init__(self, key, sum_, left=None, right=None, parent=None):
        self.key = key
        self.sum = sum_
        self.left = left
        self.right = right
        self.parent = parent

def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left else 0) + (v.right.sum if v.right else 0)
    if v.left:
        v.left.parent = v
    if v.right:
        v.right.parent = v

def small_rotation(v):
    parent = v.parent
    if not parent:
        return
    grandparent = parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v

def big_rotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        small_rotation(v.parent)
        small_rotation(v)
    else:
        small_rotation(v)
        small_rotation(v)

def splay(root, v):
    if v is None:
        return root
    while v.parent:
        if not v.parent.parent:
            small_rotation(v)
            break
        big_rotation(v)
    return v

def find(root, key):
    v = root
    last = root
    next_ = None
    while v:
        if v.key >= key and (next_ is None or v.key < next_.key):
            next_ = v
        last = v
        if v.key == key:
            break
        v = v.right if v.key < key else v.left
    root = splay(root, last)
    return next_, root

def split(root, key):
    result, root = find(root, key)
    if result is None:
        return root, None
    root = splay(root, result)
    left = root.left
    root.left = None
    if left:
        left.parent = None
    update(left)
    update(root)
    return left, root

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    min_right = right
    while min_right.left:
        min_right = min_right.left
    right = splay(right, min_right)
    right.left = left
    update(right)
    return right

class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        left, right = split(self.root, key)
        if not right or right.key != key:
            new_vertex = Vertex(key, key)
            self.root = merge(merge(left, new_vertex), right)
        else:
            self.root = merge(left, right)

    def erase(self, key):
        res, self.root = find(self.root, key)
        if res and res.key == key:
            left, middle = split(self.root, key)
            middle, right = split(middle, key + 1)
            self.root = merge(left, right)

    def find(self, key):
        res, self.root = find(self.root, key)
        return res is not None and res.key == key

    def sum(self, frm, to):
        left, middle = split(self.root, frm)
        middle, right = split(middle, to + 1)
        ans = middle.sum if middle else 0
        self.root = merge(left, merge(middle, right))
        return ans

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    MODULO = 1000000001
    last_sum_result = 0
    st = SplayTree()

    n = int(data[0])
    idx = 1

    for _ in range(n):
        if data[idx] == '+':
            x = int(data[idx + 1])
            st.insert((x + last_sum_result) % MODULO)
            idx += 2
        elif data[idx] == '-':
            x = int(data[idx + 1])
            st.erase((x + last_sum_result) % MODULO)
            idx += 2
        elif data[idx] == '?':
            x = int(data[idx + 1])
            found = st.find((x + last_sum_result) % MODULO)
            print("Found" if found else "Not found")
            idx += 2
        elif data[idx] == 's':
            l = int(data[idx + 1])
            r = int(data[idx + 2])
            res = st.sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
            print(res)
            last_sum_result = res % MODULO
            idx += 3
