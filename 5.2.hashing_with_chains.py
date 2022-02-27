# input parameters:
# m - hash table size
# requests - list of requests like "add", "del", "find", "check"
def process_requests(m, requests):

    # getting hash from string str
    def get_hash(str):

        while len(powers_x) < len(str):
            next_pow = (powers_x[-1] * x) % p
            powers_x.append(next_pow)

        rez = 0
        for i, s in enumerate(str):
            step = (ord(s) * powers_x[i]) % p
            rez = (rez + step) % p

        return rez % m

    x = 263
    p = 1000000007
    powers_x = [1]

    # output: results of "find" and "check" requests
    output = []

    # initialize the hash table
    hash_table = [[] for _ in range(m)]

    # process requests
    for req in requests:
        operation, param = req[0], req[1]

        # process the request "add string"
        if operation == "add":
            chain = hash_table[get_hash(param)]
            if param not in chain:
                chain.append(param)

        # process the request "del string"
        elif operation == "del":
            chain = hash_table[get_hash(param)]
            if param in chain:
                chain.remove(param)

        # process the request "find string"
        elif operation == "find":
            chain = hash_table[get_hash(param)]
            output.append("yes" if param in chain else "no")

        # process the request "check i"
        elif operation == "check":
            chain = hash_table[int(param)]
            output.append(" ".join(reversed(chain)))

    return output


def main():

    # read hash table size and number of requests
    m, n = int(input()), int(input())

    # read requests
    requests = []
    for _ in range(n):
        requests.append(input().split())

    # display requests "find" and "check" results
    print("\n".join(process_requests(m, requests)))


def test():
    assert process_requests(5, [('add', 'world'), ('add', 'HellO'), ('check', '4'),('find', 'World')
                            , ('find', 'world'), ('del', 'world'), ('check', '4'), ('del', 'HellO')
                            , ('add', 'luck'), ('add', 'GooD'), ('check', '2'), ('del', 'good')]) == \
                            ['HellO world', 'no', 'yes', 'HellO', 'GooD luck']


if __name__ == "__main__":
    main()