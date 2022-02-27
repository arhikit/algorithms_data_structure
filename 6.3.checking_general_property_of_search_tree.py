import sys

sys.setrecursionlimit(10 ** 5)

# describe a class for working with a search tree
class SearchTree:
    def __init__(self, tree):
        self.tree = tree

    def value(self, node):
        return self.tree[node][0]

    def left(self, node):
        return self.tree[node][1]

    def right(self, node):
        return self.tree[node][2]

    def check(self, node=0, min=-2 ** 32, max=2 ** 32):

        # if the current vertex does not exist,
        # back along the chain of recursive calls
        if node == -1:
            return True

        # compare the current vertex with its parents
        v = self.value(node)
        if v < min or v >= max:
            return False

        # call the check for the left and right sons
        return self.check(self.left(node), min, v) and self.check(self.right(node), v, max)


def checking_general_property_of_search_tree(tree):
    return 'CORRECT' if len(tree.tree) == 0 or tree.check() else 'INCORRECT'


def main():

    # read tree
    # each vertex contains info (value, left, right):
    # value - the key of the vertex,
    # left - the index of the left son of the vertex,
    # right - the index of the right son of the vertex
    tree = SearchTree([tuple(map(int, input().split())) for _ in range(int(input()))])
    print(checking_general_property_of_search_tree(tree))


def test():
    assert checking_general_property_of_search_tree(SearchTree([(2, 1, 2), (1, -1, -1), (3, -1, -1)])) \
           == "CORRECT"
    assert checking_general_property_of_search_tree(SearchTree([(1, 1, 2), (2, -1, -1), (3, -1, -1)])) \
           == "INCORRECT"
    assert checking_general_property_of_search_tree(SearchTree([(2, 1, 2), (1, -1, -1), (2, -1, -1)])) \
           == "CORRECT"
    assert checking_general_property_of_search_tree(SearchTree([(2, 1, 2), (2, -1, -1), (3, -1, -1)])) \
           == "INCORRECT"
    assert checking_general_property_of_search_tree(SearchTree([(2147483647, -1, -1)])) \
           == "CORRECT"
    assert checking_general_property_of_search_tree(SearchTree([(1, -1, 1), (2, -1, 2), (3, -1, 3), (4, -1, 4), (5, -1, -1)])) \
           == "CORRECT"
    assert checking_general_property_of_search_tree(SearchTree([(4, 1, 2), (2, 3, 4), (6, 5, 6), (1, -1, -1),
                                                        (3, -1, -1), (5, -1, -1), (7, -1, -1)])) \
           == "CORRECT"


if __name__ == "__main__":
    main()