def check(s):
    from collections import deque

    braces = {')': '(', '}': '{', ']': '['}
    stack = deque()
    for i, c in enumerate(s, start=1):
        #  if an opening parenthesis is passed, push it onto the stack
        if c in braces.values():
            stack.append((c, i))

        # if a closing bracket is passed, check it:
        # 1. stack with opening brackets can be empty
        # 2. the last opening brace may not match the closing brace
        elif c in braces and (not stack or braces[c] != stack.pop()[0]):
            return i

    # if the stack is not empty, return the last opening parenthesis.
    return stack.pop()[1] if stack else 'Success'


def main():
    # get string to test
    s = input()
    # check the given string
    print(check(s))


def test():
    assert check("([](){([])})") == "Success"
    assert check("()[]}") == 5
    assert check("{{[()]]") == 7
    assert check("{{{[][][]") == 3
    assert check("{*{{}") == 3
    assert check("[[*") == 2
    assert check("{*}") == "Success"
    assert check("{{") == 2
    assert check("{}") == "Success"
    assert check("") == "Success"
    assert check("}") == 1
    assert check("*{}") == "Success"
    assert check("{{{**[][][]") == 3


if __name__ == "__main__":
    main()
    #test()