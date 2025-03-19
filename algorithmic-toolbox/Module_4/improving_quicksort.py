import random
from typing import List, Tuple

def partition2(arr: List[int], left: int, right: int) -> int:
    """標準的 QuickSort 雙向分割法"""
    pivot = arr[left]
    j = left
    for i in range(left + 1, right + 1):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j

def partition3(arr: List[int], left: int, right: int) -> Tuple[int, int]:
    """三向切分 (3-way partition) 處理重複元素"""
    pivot = arr[left]
    j = left
    k = right

    # 將小於 pivot 的元素移到左側
    for i in range(left, right + 1):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    # 將大於 pivot 的元素移到右側
    for i in range(right, left - 1, -1):
        if arr[i] > pivot:
            arr[i], arr[k] = arr[k], arr[i]
            k -= 1

    # 將 pivot 值填充中間區域
    for i in range(j, k + 1):
        arr[i] = pivot

    return j, k

def improving_quicksort(arr: List[int], left: int, right: int) -> None:
    """隨機化快速排序"""
    if left >= right:
        return

    k = left + random.randint(0, right - left)
    arr[left], arr[k] = arr[k], arr[left]
    m1, m2 = partition3(arr, left, right)

    improving_quicksort(arr, left, m1 - 1)
    improving_quicksort(arr, m2 + 1, right)

def main():
    """主程式"""
    n = int(input())  # 讀取陣列長度
    arr = list(map(int, input().split()))  # 讀取陣列數據
    improving_quicksort(arr, 0, len(arr) - 1)  # 執行快排
    print(" ".join(map(str, arr)))  # 輸出排序後的陣列

if __name__ == "__main__":
    main()
