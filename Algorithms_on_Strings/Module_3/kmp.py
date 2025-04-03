# python3

def compute_prefix_function(pattern):
    prefix = [0] * len(pattern)
    border = 0
    for i in range(1, len(pattern)):
        while border > 0 and pattern[i] != pattern[border]:
            border = prefix[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        prefix[i] = border
    return prefix

def find_pattern_occurrences(pattern, text):
    combined = pattern + '$' + text
    prefix = compute_prefix_function(combined)
    pattern_len = len(pattern)
    result = []
    for i in range(pattern_len + 1, len(combined)):
        if prefix[i] == pattern_len:
            result.append(i - 2 * pattern_len)
    return result

if __name__ == "__main__":
    pattern = input().strip()
    text = input().strip()
    print(*find_pattern_occurrences(pattern, text))
