# input parameters:
# n - number of tables
# r - table sizes
# requests - requests for joining tables
def concatenation_of_tables(n, r, requests):

    # find the id of a set containing table i
    def find(i):
        # use path compression
        if i != parent[i]:
            parent[i] = find(parent[i])
        return parent[i]

    # combine sets containing table i and table j
    # return the maximum size of the sets
    def union(i, j, current_max):
        id_i, id_j = find(i), find(j)

        if id_i != id_j:
            if rank[id_i] > rank[id_j]:
                parent[id_j] = id_i
                r[id_i] += r[id_j]
                current_max = max(current_max, r[id_i])

            else:
                parent[id_i] = id_j
                r[id_j] += r[id_i]
                current_max = max(current_max, r[id_j])

                if rank[id_i] == rank[id_j]:
                    rank[id_j] += 1

        return current_max

    # set parent ids
    parent = [i for i in range(n)]
    # set set heights of subtrees
    # rank[i] >= height of the subtree rooted at node i
    rank = [0 for _ in range(n)]

    # calculate the maximum size of tables
    current_max = max(r)

    # output: the max size of tables at each step
    output = []

    # process the list of requests for joining tables
    for destination, source in requests:

        # calculate and store the current max table size
        current_max = union(destination - 1, source - 1, current_max)
        output.append(current_max)

    return output


def main():

    # read the number of tables and the number of requests
    n, m = map(int, input().split())

    # read table sizes
    r = list(map(int, input().split()))

    # read requests
    requests = []
    for _ in range(m):
        destination, source = map(int, input().split())
        requests.append((destination, source))

    # perform the table concatenation
    print("\n".join(map(str, concatenation_of_tables(n, r, requests))))


def test():
    assert concatenation_of_tables(5, [1, 1, 1, 1, 1], [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)]) == [2, 2, 3, 5, 5]
    assert concatenation_of_tables(6, [10, 0, 5, 0, 3, 3], [(6, 6), (6, 5), (5, 4), (4, 3)]) == [10, 10, 10, 11]


if __name__ == "__main__":
    main()