import sys
from typing import List

def optimal_sequence(n: int) -> List[int]:
    """計算將 n 轉換為 1 所需的最少操作次數，並回溯操作路徑"""
    array = [sys.maxsize] * (n + 1)
    array[1] = 0  # 對於 n=1，不需要任何操作

    for i in range(2, n + 1):
        a1 = array[i - 1] + 1  # 減 1 操作
        m2 = array[i // 2] + 1 if i % 2 == 0 else sys.maxsize  # 除以 2
        m3 = array[i // 3] + 1 if i % 3 == 0 else sys.maxsize  # 除以 3
        array[i] = min(a1, m2, m3)  # 取最小操作次數

    # 回溯找出最佳操作路徑
    sequences = []
    while n > 1:
        sequences.append(n)
        if n % 3 == 0 and array[n // 3] + 1 == array[n]:
            n //= 3
        elif n % 2 == 0 and array[n // 2] + 1 == array[n]:
            n //= 2
        else:
            n -= 1
    sequences.append(1)

    return sequences[::-1]  # 反轉結果，使其從 1 到 n

def main():
    """主程式"""
    n = int(input())  # 讀取輸入數字
    sequence = optimal_sequence(n)  # 計算最佳路徑

    print(len(sequence) - 1)  # 輸出最少操作次數
    print(" ".join(map(str, sequence)))  # 輸出從 1 到 n 的路徑

if __name__ == "__main__":
    main()
