# input parameters:
# n - number of processors
# m - number of tasks
# t - time required to process tasks
def parallel_processing(n, m, t):

    # get the index of the left child
    def left_child(i):
        return 2 * i + 1

    # get the index of the right child
    def right_child(i):
        return 2 * i + 2

    # sift down the element with index i
    def sift_down(i):

        # get the indices of the left and right childs
        max_index, l, r = i, left_child(i), right_child(i)

        # find the minimum of three elements:
        # first we compare the release times,
        # if they are equal, we take the processor with the min id
        if l < size_heap \
                and (heap[l][1] < heap[max_index][1]
                     or heap[l][1] == heap[max_index][1] and heap[l][0] < heap[max_index][0]):
            max_index = l
        if r < size_heap \
                and (heap[r][1] < heap[max_index][1]
                     or heap[r][1] == heap[max_index][1] and heap[r][0] < heap[max_index][0]):
            max_index = r

        # swap elements
        if i != max_index:
            heap[i], heap[max_index] = heap[max_index], heap[i]
            sift_down(max_index)

    # create an initial heap for storing processor information
    # heap element - pair (processor id, processor release time)
    # heap size - min (number of processors, number of tasks)
    size_heap = min(n, m)
    heap = [(i, t[i]) for i in range(size_heap)]

    # keep the order of processing tasks
    queue = [(i, 0) for i in range(size_heap)]

    # build min-heap
    # all non-sheet elements must be sieved down
    for i in range((size_heap - 1)// 2, -1, -1):
        sift_down(i)

    # process tasks with numbers from n to m-1
    for i in range(n, m):

        # get the min heap element (the first free processor)
        # and put its id and release time in the queue
        queue.append(heap[0])

        # change the release time of the first processor
        heap[0] = (heap[0][0], heap[0][1] + t[i])
        sift_down(0)

    # return the task processing queue
    # - pair (processor id, time of accepting the task for work)
    return queue


def main():

    # read the number of processors and the number of tasks
    n, m = map(int, input().split())

    # read the time required to process tasks
    t = list(map(int, input().split()))

    # perform parallel processing of tasks
    queue = parallel_processing(n, m, t)

    # display the task processing queue
    # - pair (processor id, time of accepting the task for work)
    for step in queue:
        print(*step)


def test():
    assert parallel_processing(2, 5, [1, 2, 3, 4, 5]) == [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]
    assert parallel_processing(4, 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2)]


if __name__ == "__main__":
    main()