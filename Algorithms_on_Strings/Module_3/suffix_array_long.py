# python3

ALPHABET_SIZE = 5

def get_index(c):
    return {'A': 1, 'C': 2, 'G': 3, 'T': 4}.get(c, 0)

def counting_sort(s):
    count = [0] * ALPHABET_SIZE
    order = [0] * len(s)

    for c in s:
        count[get_index(c)] += 1

    for j in range(1, ALPHABET_SIZE):
        count[j] += count[j - 1]

    for i in reversed(range(len(s))):
        c = s[i]
        idx = get_index(c)
        count[idx] -= 1
        order[count[idx]] = i

    return order

def compute_classes(s, order):
    cclass = [0] * len(s)
    for i in range(1, len(s)):
        cur, prev = order[i], order[i - 1]
        if s[cur] != s[prev]:
            cclass[cur] = cclass[prev] + 1
        else:
            cclass[cur] = cclass[prev]
    return cclass

def sort_doubled(s, L, order, cclass):
    count = [0] * len(s)
    new_order = [0] * len(s)

    for cl in cclass:
        count[cl] += 1

    for j in range(1, len(s)):
        count[j] += count[j - 1]

    for i in reversed(range(len(s))):
        start = (order[i] - L + len(s)) % len(s)
        cl = cclass[start]
        count[cl] -= 1
        new_order[count[cl]] = start

    return new_order

def update_classes(new_order, cclass, L):
    n = len(new_order)
    new_cclass = [0] * n

    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, mid_prev = (cur + L) % n, (prev + L) % n

        if cclass[cur] != cclass[prev] or cclass[mid] != cclass[mid_prev]:
            new_cclass[cur] = new_cclass[prev] + 1
        else:
            new_cclass[cur] = new_cclass[prev]

    return new_cclass

def build_suffix_array(s):
    order = counting_sort(s)
    cclass = compute_classes(s, order)
    L = 1
    while L < len(s):
        order = sort_doubled(s, L, order, cclass)
        cclass = update_classes(order, cclass, L)
        L *= 2
    return order

if __name__ == "__main__":
    s = input().strip()
    print(' '.join(map(str, build_suffix_array(s))))
