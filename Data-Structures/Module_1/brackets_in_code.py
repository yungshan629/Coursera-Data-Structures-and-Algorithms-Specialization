def is_balanced(s):
    checking_stack = []

    for i, char in enumerate(s):
        if char in '[{(':
            checking_stack.append((char, i))
        elif char in ']})':
            if not checking_stack:
                return str(i + 1)
            top, idx = checking_stack.pop()
            if (top == '[' and char != ']') or (top == '{' and char != '}') or (top == '(' and char != ')'):
                return str(i + 1)

    return "Success" if not checking_stack else str(checking_stack[-1][1] + 1)


if __name__ == "__main__":
    input_str = input()
    print(is_balanced(input_str))
