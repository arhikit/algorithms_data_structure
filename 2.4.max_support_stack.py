def process_requests(n, requests):

    # put only the maximums on the stack,
    # since the values themselves are not needed
    stack = [0]

    # output: results of "max" requests
    output = []

    for req in requests:

        if req == "max":
            output.append(stack[-1])

        if req == "pop":
            stack.pop()

        if "push" in req:
            stack.append(max(stack[-1], int(req.split()[1])))

    return output


def main():

    # read the number of requests
    n = int(input())

    # read requests
    requests = []
    for req in (input() for _ in range(n)):
        requests.append(req)

    # for each "max" request, we display the maximum number on the stack
    print("\n".join(map(str, process_requests(n, requests))))


def test():
    assert process_requests(3, ["push 1", "push 7", "pop"]) == []
    assert process_requests(5, ["push 2", "push 1", "max", "pop", "max"]) == [2, 2]
    assert process_requests(6, ["push 7", "push 1", "push 7", "max", "pop", "max"]) == [7, 7]
    assert process_requests(5, ["push 1", "push 2", "max", "pop", "max"]) == [2, 1]
    assert process_requests(10, ["push 2", "push 3", "push 9", "push 7", "push 2", "max", "max", "max", "pop", "max"]) == [9, 9, 9, 9]


if __name__ == "__main__":
    main()