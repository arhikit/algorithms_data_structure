def build_heap(n, a):

    # get the index of the left child
    def left_child(i):
        return 2 * i + 1

    # get the index of the right child
    def right_child(i):
        return 2 * i + 2

    # sift down the element with index i
    def sift_down(i, steps):

        # get the indices of the left and right childs
        max_index, l, r = i, left_child(i), right_child(i)

        # find the minimum of three elements
        if l < n and a[l] < a[max_index]: max_index = l
        if r < n and a[r] < a[max_index]: max_index = r

        # swap elements
        if i != max_index:
            steps.append((i, max_index))
            a[i], a[max_index] = a[max_index], a[i]
            sift_down(max_index, steps)

    # save all steps of exchanges
    steps = []

    # all non-sheet elements must be sieved down
    for i in range((n - 1) // 2, -1, -1):
        sift_down(i, steps)

    return steps


def main():

    # read array size and array
    n = int(input())
    a = list(map(int, input().split()))

    # build heap
    steps = build_heap(n, a)

    # displaying all steps of exchanges
    print(len(steps))
    for step in steps:
        print(*step)


def test():
    assert build_heap(5, [5, 4, 3, 2, 1]) == [(1, 4), (0, 1), (1, 3)]
    assert build_heap(5, [1, 2, 3, 4, 5]) == []
    assert build_heap(6, [7, 6, 5, 4, 3, 2]) == [(2, 5), (1, 4), (0, 2), (2, 5)]


if __name__ == "__main__":
    test()