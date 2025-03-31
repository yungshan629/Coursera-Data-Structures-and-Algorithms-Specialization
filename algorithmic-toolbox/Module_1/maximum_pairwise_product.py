def maximum_pairwise_product(numbers: list[int]) -> int:
    numbers.sort()
    return numbers[-1]*numbers[-2]

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int,input().split()))
    print(maximum_pairwise_product(numbers))