# python3

def inverse_bwt(bwt: str) -> str:
    n = len(bwt)

    # Step 1: 統計每個字元的出現次數，並建立排名（rank）
    counts = {}
    ranks = []
    for c in bwt:
        counts[c] = counts.get(c, 0) + 1
        ranks.append(counts[c])

    # Step 2: 建立 first column 的起始位置（prefix sum）
    sorted_chars = sorted(counts.keys())
    starts = {}
    total = 0
    for c in sorted_chars:
        starts[c] = total
        total += counts[c]

    # Step 3: 找出 '$' 在 BWT 中的位置（作為起點）
    dollar_index = bwt.index('$')

    # Step 4: 依據 LF-mapping 重建原始字串
    result = []
    idx = dollar_index
    for _ in range(n):
        c = bwt[idx]
        result.append(c)
        idx = starts[c] + ranks[idx] - 1

    # Step 5: 反轉後即為原始字串
    return ''.join(result[::-1])


if __name__ == "__main__":
    bwt = input().strip()
    print(inverse_bwt(bwt))
