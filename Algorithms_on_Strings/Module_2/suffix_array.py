# python3

def build_suffix_array(text):
   
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()
    return [pos for _, pos in suffixes]


if __name__ == "__main__":
    text = input().strip()
    suffix_array = build_suffix_array(text)
    print(" ".join(map(str, suffix_array)))
