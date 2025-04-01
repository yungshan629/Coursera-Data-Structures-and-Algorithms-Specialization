# python3

def is_substring(sub, string):
    """Check if sub is a substring of string."""
    return sub in string

def find_shortest_non_shared_substring(s, t):
    # Try all possible lengths of substrings, starting from 1
    for length in range(1, len(s) + 1):
        # Check all substrings of s with the current length
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            # If this substring is not in t, return it
            if not is_substring(substring, t):
                return substring
    
    # If no non-shared substring is found
    return ""

if __name__ == "__main__":
    text1 = input().strip()
    text2 = input().strip()
    print(find_shortest_non_shared_substring(text1, text2))