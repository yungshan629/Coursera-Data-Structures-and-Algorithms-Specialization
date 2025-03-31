def gcd(a, b):
    while b:
        a, b = b, a%b
    
    return a

def lcm(a,b):
    e = gcd(a, b)

    return int(a*b/e)
     


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))