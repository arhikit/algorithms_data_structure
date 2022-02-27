# input parameters:
# n - number of variables
# equalities - equalities of the form x_i = x_j
# inequalities - inequalities of the form x_i != x_j
def automatic_program_analysis(n, equalities, inequalities):

    # find the id of a set containing variable i
    def find(i):
        # use path compression
        if i != parent[i]:
            parent[i] = find(parent[i])
        return parent[i]

    # combine sets containing variable i and variable j
    def union(i, j):
        id_i, id_j = find(i), find(j)

        if id_i != id_j:
            if rank[id_i] > rank[id_j]:
                parent[id_j] = id_i
            else:
                parent[id_i] = id_j
                if rank[id_i] == rank[id_j]:
                    rank[id_j] += 1

    # set parent ids
    parent = [i for i in range(n)]
    # set set heights of subtrees
    # rank[i] >= height of the subtree rooted at node i
    rank = [0 for _ in range(n)]

    # process equalities
    for x_i, x_j in equalities:
        # union variables x_i and x_j into one set
        union(x_i - 1, x_j - 1)

    # process equalities
    for x_i, x_j in inequalities:

        # if the variables x_i and x_j belong to the same set, return 0
        if find(x_i - 1) == find(x_j - 1):
            return 0

    return 1


def main():

    # read the number of variables, the number of equalities and the number of inequalities
    n, e, d = map(int, input().split())

    # read equalities
    equalities = []
    for _ in range(e):
        x_i, x_j = map(int, input().split())
        equalities.append((x_i, x_j))

    # read inequalities
    inequalities = []
    for _ in range(d):
        x_i, x_j = map(int, input().split())
        inequalities.append((x_i, x_j))

    # perform automatic program analysis
    print(automatic_program_analysis(n, equalities, inequalities))


def test():
    assert automatic_program_analysis(4, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], []) == 1
    assert automatic_program_analysis(6, [(2, 3), (1, 5), (2, 5), (3, 4), (4, 2)], [(6, 1), (4, 6), (4, 5)]) == 0


if __name__ == "__main__":
    main()