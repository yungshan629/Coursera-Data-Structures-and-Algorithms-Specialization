import random
import time

class Data:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text

def read_input():
    pattern = input()
    text = input()
    return Data(pattern, text)

def print_output(output):
    for i in reversed(output):
        print(i, end=" ")
    print()

def hash_function(s, prime, x):
    hash_value = 0
    for c in reversed(s):
        hash_value = (hash_value * x + ord(c)) % prime
    return hash_value

def precompute_hashes(T, t_substr, pattern_size, prime, x):
    text_size = len(T)
    H = [0] * (text_size - pattern_size + 1)
    H[text_size - pattern_size] = hash_function(t_substr, prime, x)
    
    y = 1
    for i in range(1, pattern_size + 1):
        y = (y * x) % prime

    for i in range(text_size - pattern_size - 1, -1, -1):
        H[i] = (H[i + 1] * x + ord(T[i]) - y * ord(T[i + pattern_size])) % prime

    return H

def rabin_karp(data):
    p = data.pattern
    t = data.text

    prime = 100000007
    x = random.randint(1, prime - 1)

    pattern_size = len(p)
    text_size = len(t)

    pattern_hash = hash_function(p, prime, x)
    t_substr = t[text_size - pattern_size:]
    H = precompute_hashes(t, t_substr, pattern_size, prime, x)

    for i in range(text_size - pattern_size + 1):
        if H[i] == pattern_hash and t[i:i + pattern_size] == p:
            print(i, end=" ")

    print()

if __name__ == "__main__":
    data = read_input()
    rabin_karp(data)
