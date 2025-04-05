def fractional_knapsack(capacity: int, items: list[tuple[int, int]]) -> float:
    # 加上每項物品的 per_value
    items.sort(key=lambda x: x[0] / x[1], reverse=True)  # 按單位價值排序
    
    total_value = 0
    i = 0
    while capacity > 0 and i< len(items):
        cost, weight = items[i]
        if capacity >= weight:
            capacity -= weight
            total_value += cost
            i += 1
        else:
            total_value += cost/weight*capacity
            capacity = 0

    return total_value




def main():
    """主程式：讀取輸入並執行演算法"""
    n, capacity = map(int, input().split())
    items = []
    for _ in range(n):
        cost, weight = map(int, input().split())
        items.append((cost, weight))

    result = fractional_knapsack(capacity, items)
    print(f"{result:.4f}")


if __name__ == "__main__":
    main()
