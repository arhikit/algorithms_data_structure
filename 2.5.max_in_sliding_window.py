def get_max_in_sliding_window(n, a, m):

    from collections import deque

    # output: max in sliding window
    output = []

    # a queue to store the maximum items in the sliding window.
    # the first element of the queue is the maximum in the current window,
    # next are the elements being processed
    que = deque()

    # loop through all the elements of the list a
    for i in range(n):

        # starting from element m, shift the window 1 position to the right.
        # if the "leaving from the left" element of the list was equal to the first element of the queue,
        # remove the first element from the queue
        if i >= m and que[0] == a[i - m]:
            que.popleft()

        # until the queue isn't empty and the last element of the queue is less than the current element,
        # remove the last item from the queue
        while que and que[-1] < a[i]:
            que.pop()

        # add the current item to the queue
        que.append(a[i])

        # starting with m - 1 element, output the first element of the queue (= maximum element in the sliding window)
        if i >= m - 1:
            output.append(que[0])

    return " ".join(map(str, output))

def main():

    # read array size, array and window width
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    # find the maximum in a sliding window of size m for array a
    print(get_max_in_sliding_window(n, a, m))


def test():
    assert get_max_in_sliding_window(8, [2, 7, 3, 1, 5, 2, 6, 2], 4) == "7 7 5 6 6"
    assert get_max_in_sliding_window(3, [2, 1, 5], 1) == "2 1 5"
    assert get_max_in_sliding_window(3, [2, 3, 9], 3) == "9"


if __name__ == "__main__":
    main()