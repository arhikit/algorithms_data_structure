def build_tree_traversals(tree):

    def order(node, actions):

        for a in actions:
            elem = tree[node][a]

            yield from (order(elem, actions) if elem != -1 else ()) if a else (elem,)
            #if a == 0:
            #    yield elem
            #elif elem != -1:
            #    yield from order(elem, actions)

    output = []

    # in_order
    output.append(tuple(order(0, [1, 0, 2])))

    # pre_order
    output.append(tuple(order(0, [0, 1, 2])))

    # post_order
    output.append(tuple(order(0, [1, 2, 0])))

    return output


def main():

    # read tree
    # each vertex contains info (key, left, right):
    # key - the key of the vertex,
    # left - the index of the left son of the vertex,
    # right - the index of the right son of the vertex
    tree = [tuple(map(int, input().split())) for _ in range(int(input()))]

    # build in-order, pre-order, and post-order traversals of a binary tree.
    print("\n".join( map(lambda order: " ".join(map(str, order)), build_tree_traversals(tree))))


def test():
    assert build_tree_traversals([(4, 1, 2), (2, 3, 4), (5, -1, -1), (1, -1, -1), (3, -1, -1)]) \
           == [(1, 2, 3, 4, 5), (4, 2, 1, 3, 5), (1, 3, 2, 5, 4)]
    assert build_tree_traversals([(0, 7, 2), (10, -1, -1), (20, -1, 6), (30, 8, 9), (40, 3, -1),
                         (50, -1, -1), (60, 1, -1), (70, 5, 4), (80, -1, -1), (90, -1, -1)]) \
           == [(50, 70, 80, 30, 90, 40, 0, 20, 10, 60),
               (0, 70, 50, 40, 30, 80, 90, 20, 60, 10),
               (50, 80, 90, 30, 40, 70, 10, 60, 20, 0)]


if __name__ == "__main__":
    main()