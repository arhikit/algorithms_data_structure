def checking_property_of_search_tree(tree):

    if not tree: return 'CORRECT'

    # implement in_order tree traversal without using recursion

    # start traversing from the root of the tree
    i = 0

    # prev - the value of the previous vertex when traversing in_order
    prev = -2 ** 32

    # use a stack to store the traversed vertices
    # that are to the right of the current vertex
    stack = []

    # while the current vertex exists
    # or there are vertices in the stack
    while i > -1 or stack:

        # if the current vertex exists
        if i > -1:

            # add the current vertex to the stack
            stack.append(i)

            # go to the left son
            i = tree[i][1]

        # if the current vertex does not exist
        else:

            # take the top vertex from the stack
            i = stack.pop()

            # if the previous value is greater than the value of the current vertex,
            # the property of the search tree is not executed
            if prev > tree[i][0]: return 'INCORRECT'

            # change the previous value
            prev = tree[i][0]

            # go to the right son
            i = tree[i][2]

    return 'CORRECT'


def main():

    # read tree
    # each vertex contains info (key, left, right):
    # key - the key of the vertex,
    # left - the index of the left son of the vertex,
    # right - the index of the right son of the vertex
    tree = [tuple(map(int, input().split())) for _ in range(int(input()))]

    print(checking_property_of_search_tree(tree))


def test():
    assert checking_property_of_search_tree([(2, 1, 2), (1, -1, -1), (3, -1, -1)]) \
           == "CORRECT"
    assert checking_property_of_search_tree([(1, 1, 2), (2, -1, -1), (3, -1, -1)]) \
           == "INCORRECT"
    assert checking_property_of_search_tree([]) \
           == "CORRECT"
    assert checking_property_of_search_tree([(1, -1, 1), (2, -1, 2), (3, -1, 3), (4, -1, 4), (5, -1, -1)]) \
           == "CORRECT"
    assert checking_property_of_search_tree([(4, 1, 2), (2, 3, 4), (6, 5, 6), (1, -1, -1),
                                             (3, -1, -1), (5, -1, -1), (7, -1, -1)]) \
           == "CORRECT"
    assert checking_property_of_search_tree([(4, 1, -1), (2, 2, 3), (1, -1, -1), (5, -1, -1)]) \
           == "INCORRECT"


if __name__ == "__main__":
    main()