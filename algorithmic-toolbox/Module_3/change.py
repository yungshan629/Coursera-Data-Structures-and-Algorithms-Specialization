def change(m: int) -> int:
    """計算最少硬幣數量來湊出金額 m"""
    n10 = m // 10  # 使用 10 元硬幣
    n1 = m % 10
    n5 = n1 // 5  # 使用 5 元硬幣
    n1 = n1 % 5
    
    return n1 + n5 + n10

def main():
    """主程式"""
    m = int(input())  
    print(change(m))  

if __name__ == "__main__":
    main()
