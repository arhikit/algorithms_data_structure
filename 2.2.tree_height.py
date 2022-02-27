# solution through the list of parents (bottom-up)
def get_height(in1, in2):

    # get the number of vertices and the list of parents
    n = int(in1)
    parents = list(map(int, in2.split(" ")))

    # set a dictionary to store the distances from the vertex to the root (tree levels)
    levels = {}

    # go up the tree and count the level of the vertex
    def up(v):
        parent = parents[v]
        if parent == -1:
            return 1
        if v not in levels:
            levels[v] = up(parent) + 1
        return levels[v]

    # find the maximum level of the vertices by going through all the vertices
    max_level = 0
    for v in range(n):
        max_level = max(max_level, up(v))

    return max_level


# solution through the list of children (top-down)
def get_height_2(in1, in2):
    from collections import deque

    # get the number of vertices and the list of parents
    n = int(in1)
    parents = list(map(int, in2.split(" ")))

    # according to the list of parents, we build a list of children and get the root number
    graph = [[] for _ in range(n)]
    num_root = -1
    for i, v in enumerate(parents):
        if v != -1:
            graph[v].append(i)
        else:
            num_root = i

    # initialize the stack
    q = deque()
    # put the root on the stack
    q.append((num_root, 1))
    max_height = 1

    # until the queue is empty
    while q:
        # retrieve the first element of the queue
        head = q.popleft()

        # if there are child elements
        if graph[head[0]]:
            height = head[1] + 1

            # iterate through all the child elements and queue them up
            # while increasing the height index in parallel
            for child in graph[head[0]]:
               q.append((child, height))
            max_height = max(max_height, height)

    return max_height


def main():
    # get the height of the tree
    print(get_height(input(), input()))
    #print(get_height_2(input(), input()))


def test():
    assert get_height("10", "9 7 5 5 2 9 9 9 2 -1") == 4


if __name__ == "__main__":
    main()
    # test()