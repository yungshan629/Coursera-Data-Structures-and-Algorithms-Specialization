def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    digit = [0, 1, 2, 6, 5, 0, 4, 3, 4, 0, 5, 6, 2, 1, 0, 0, 9, 8, 4, 5, 0, 6, 7, 6, 0, 5, 4, 8, 9, 0, 0, 1, 2, 6, 5, 0, 4, 3, 4, 0, 5, 6, 2, 1, 0, 0, 9, 8, 4, 5, 0, 6, 7, 6, 0, 5, 4, 8, 9, 0] 

    i = n % 60
    
    return digit[i]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
