from typing import List

def lcs2(a: List[int], b: List[int]) -> int:
    """計算兩個序列的最長共同子序列 (LCS) 長度"""
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]  # 兩個元素相等時，LCS +1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 取較長的子序列

    return dp[len(a)][len(b)]

def main():
    """主程式"""
    n = int(input())  # 讀取第一個序列長度
    a = list(map(int, input().split()))  # 讀取第一個序列

    m = int(input())  # 讀取第二個序列長度
    b = list(map(int, input().split()))  # 讀取第二個序列

    print(lcs2(a, b))  # 計算 LCS 長度並輸出

if __name__ == "__main__":
    main()
