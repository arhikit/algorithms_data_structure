def check(s):
    from collections import deque

    braces = {')': '(', '}': '{', ']': '['}
    stack = deque()
    for i, c in enumerate(s, start=1):
        #  если передана открывающаяся скобка, то кладем ее в стек
        if c in braces.values():
            stack.append((c, i))

        # если передана закрывающаяся скобка, то проверяем ее:
        # 1. стек с открывающимися скобками может быть пустой
        # 2. последняя открывающая скобка может не соответствовать закрывающейся
        elif c in braces and (not stack or braces[c] != stack.pop()[0]):
            return i

    # если стек не пуст, то возвращаем последнюю открывающуся скобку
    return stack.pop()[1] if stack else 'Success'


def main():
    # получаем строку для проверки
    s = input()
    # проверяем переданную строку
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