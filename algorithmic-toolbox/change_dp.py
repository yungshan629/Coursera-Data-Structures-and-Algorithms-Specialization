import sys

def change_dp(m: int) -> int:
    """使用動態規劃計算最少硬幣數量 (硬幣面額 1, 3, 4)"""
    changes = [sys.maxsize] * (m + 1)
    changes[0] = 0  # 0 元不需要任何硬幣

    for i in range(1, m + 1):
        c1 = changes[i - 1] + 1 if i - 1 >= 0 else sys.maxsize
        c3 = changes[i - 3] + 1 if i - 3 >= 0 else sys.maxsize
        c4 = changes[i - 4] + 1 if i - 4 >= 0 else sys.maxsize
        changes[i] = min(c1, c3, c4)

    return changes[m]

def main():
    """主程式"""
    m = int(input())  # 讀取金額
    print(change_dp(m))  # 計算最少硬幣數量

if __name__ == "__main__":
    main()
