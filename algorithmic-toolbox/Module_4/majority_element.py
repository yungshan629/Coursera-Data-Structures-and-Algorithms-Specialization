from typing import List

def majority_element(arr: List[int], left: int, right: int) -> int:
    """分治法找出多數元素 (出現次數 > n/2 的元素)"""
    if left == right:
        return arr[left]

    if left + 1 == right:
        return arr[left] if arr[left] == arr[right] else -1

    mid = left + (right - left) // 2

    x = majority_element(arr, left, mid)
    y = majority_element(arr, mid + 1, right)

    count_x, count_y = 0, 0

    for i in range(left, right + 1):
        if arr[i] == x:
            count_x += 1
        elif arr[i] == y:
            count_y += 1

    n = right - left + 1

    if count_x > count_y and count_x > n // 2:
        return x
    if count_y > count_x and count_y > n // 2:
        return y

    return -1

def main():
    """主程式"""
    n = int(input())  # 讀取數列長度
    arr = list(map(int, input().split()))  # 讀取數列
    print(1 if majority_element(arr, 0, len(arr) - 1) != -1 else 0)  # 判斷是否有多數元素

if __name__ == "__main__":
    main()
