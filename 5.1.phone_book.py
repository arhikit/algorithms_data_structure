def process_requests(requests):

    # output: results of "find" requests
    output = []

    # initialize the phone book
    book = {}

    # process requests
    for req in requests:
        operation, number = req[0], int(req[1])

        # process the request "add number name"
        if operation == "add":
            name = req[2]
            book[number] = name

        # process the request "del number"
        elif operation == "del":
            if number in book:
                del book[number]

        # process the request "find number"
        elif operation == "find":
            output.append(book[number] if number in book else "not found")

    return output


def main():

    # read the number of requests
    n = int(input())

    # read requests
    requests = []
    for _ in range(n):
        requests.append(input().split())

    # for each "find" request, display name by phone number
    print("\n".join(process_requests(requests)))


def test():
    assert process_requests([('find','3839442'), ('add','123456','me'),('add','0','granny'),('find', '0')
                            ,('find','123456'),('del','0'),('del','0'),('find', '0')]) == \
           ['not found', 'granny', 'me', 'not found']


if __name__ == "__main__":
    main()