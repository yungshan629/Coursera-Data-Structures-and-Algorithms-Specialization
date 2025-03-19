from typing import List

def binary_search(arr: List[int], left: int, right: int, x: int) -> int:
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, left, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, right, x)

def linear_search(arr: List[int], x: int) -> int:
    for i, num in enumerate(arr):
        if num == x:
            return i
    return -1

def main():
    n = int(input())  # 讀取數列 a 的大小
    a = list(map(int, input().split()))  # 讀取 n 個數
    m = int(input())  # 讀取數列 b 的大小
    b = list(map(int, input().split()))  # 讀取 m 個數
    results = [binary_search(a, 0, len(a) - 1, num) for num in b]
    print(" ".join(map(str, results)))  # 以空格輸出結果

if __name__ == "__main__":
    main()
