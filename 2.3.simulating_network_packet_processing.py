def process_packages(size, n, packages):

    # use the buffer variable to store information about packets in processing: (arrival, arrival + duration)
    buffer = [(-1, -1) for _ in range(size)]
    # initialize variables to store the current position in the array and the current arrival time
    cur_pos, cur_arr = 0, -1

    # output: packet processing time
    output = []

    # read packets line by line
    for arr, dur in ((package[0], package[1]) for package in packages):

        # shift the current arrival time
        if cur_arr < arr:
            cur_arr = arr

        # if the buffer is full when the packet arrives:
        # the current position in the buffer is full
        # and the packet arrives before the completion of the processing of the current packet,
        # then the packet will be completely discarded
        if buffer[cur_pos % size][0] != -1 and arr < buffer[cur_pos % size][1]:
            output.append(-1)
        # else put the packet in the buffer
        else:
            output.append(cur_arr)
            buffer[cur_pos % size] = (cur_arr, cur_arr + dur)
            cur_pos += 1
            cur_arr += dur

    return output


def main():
    # get buffer size and number of packets
    size, n = map(int, input().split())

    # read package list
    packages = []
    for arr, dur in (map(int, input().split()) for _ in range(n)):
        packages.append([arr, dur])

    # output the packet processing time line by line
    print("\n".join(map(str, process_packages(size, n, packages))))


def test():

    assert process_packages(1, 0, []) == []
    assert process_packages(1, 2, [[0, 1], [0, 1]]) == [0, -1]
    assert process_packages(1, 2, [[0, 1], [1, 1]]) ==[0, 1]
    assert process_packages(2, 8, [[0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 1], [1, 2], [1, 3]]) == [0, 0, 0, 1, 1, 1, 2, -1]
    assert process_packages(2, 8, [[0, 0], [0, 0], [0, 0], [1, 1], [1, 0], [1, 0], [1, 2], [1, 3]]) == [0, 0, 0, 1, 2, -1, -1, -1]
    assert process_packages(1, 5, [[999999, 1], [1000000, 0], [1000000, 1], [1000000, 0],
                            [1000000, 0]]) == [999999, 1000000, 1000000, -1, -1]
    assert process_packages(3, 6, [[0, 7], [0, 0], [2, 0], [3, 3], [4, 0], [5, 0]]) == [0, 7, 7, -1, -1, -1]
    assert process_packages(2, 6, [[0, 2], [0, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == [0, 2, 2, 3, 4, 5]
    assert process_packages(1, 25, [[16, 0], [29, 3], [44, 6], [58, 0], [72, 2],
                            [88, 8], [95, 7], [108, 6], [123, 9], [139, 6],
                            [152, 6], [157, 3], [169, 3], [183, 1], [192, 0],
                            [202, 8], [213, 8], [229, 3], [232, 3], [236, 3],
                            [239, 4], [247, 8], [251, 2], [267, 7], [275,
                                                                     7]]) == [16, 29, 44, 58, 72, 88, -1, 108, 123, 139, 152, -1, 169, 183, 192, 202, 213, 229, 232, 236, 239, 247, -1, 267, 275]
    assert process_packages(1, 25, [[15, 23], [24, 44], [39, 43], [48, 15], [56, 6],
                            [56, 8], [56, 29], [56, 28], [56, 4], [56, 17],
                            [68, 44], [75, 22], [75, 34], [84, 46], [84, 21],
                            [84, 25], [97, 31], [105, 34], [105, 43],
                            [117, 17], [129, 12], [142, 47], [144, 22],[144, 18],
                            [152, 9]]) == [15, -1, 39, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 84, -1, -1, -1, -1, -1, -1, -1, 142, -1, -1, -1]

    assert process_packages(15, 25, [[5, 11], [10, 14], [25, 17], [41, 22], [54, 36],
                            [70, 13], [81, 8], [90, 12], [103, 21], [115, 38],
                            [124, 18], [138, 15], [142, 13], [155, 31],
                            [168, 0], [177, 49], [186, 8], [196, 30],
                            [206, 37], [217, 49], [232, 31], [247, 25],
                            [260, 31], [268, 36],
                            [279, 8]]) == [5, 16, 30, 47, 69, 105, 118, 126, 138, 159, 197, 215, 230, 243, 274, 274, 323, 331, 361, 398, 447, 478, 503, 534, 570]

    assert process_packages(11, 25, [[11, 45], [26, 22], [38, 24], [42, 49], [48, 39],
                            [59, 3], [67, 1], [76, 5], [84, 30], [89, 37],
                            [99, 12], [111, 6], [125, 33], [132, 20],
                            [147, 16], [160, 7], [174, 15], [185, 14],
                            [198, 9], [200, 37], [208, 18], [222, 3],
                            [237, 28], [248, 10],
                            [263, 11]]) == [11, 56, 78, 102, 151, 190, 193, 194, 199, 229, 266, 278, 284, 317, -1, 337, -1, -1, 344, 353, 390, 408, 411, -1, -1]

    assert process_packages(13, 25, [[10, 37], [20, 45], [29, 24], [31, 17], [38, 43],
                            [49, 30], [59, 12], [72, 28], [82, 45], [91, 10],
                            [107, 46], [113, 4], [128, 16], [139, 1],
                            [149, 41], [163, 0], [172, 22], [185, 1],
                            [191, 17], [201, 3], [209, 11], [223, 30],
                            [236, 17], [252, 42],
                            [262, 0]]) == [10, 47, 92, 116, 133, 176, 206, 218, 246, 291, 301, 347, 351, 367, 368, 409, 409, 431, -1, -1, 432, 443, -1, 473, -1]

    assert process_packages(11, 25, [[6, 23], [15, 44], [24, 28], [25, 15], [33, 7],
                            [47, 41], [58, 25], [65, 5], [70, 14], [79, 8],
                            [93, 43], [103, 11], [110, 25], [123, 27],
                            [138, 40], [144, 19], [159, 2], [167, 23],
                            [179, 43], [182, 31], [186, 7], [198, 16],
                            [208, 41], [222, 23],
                            [235, 26]]) == [6, 29, 73, 101, 116, 123, 164, 189, 194, 208, 216, 259, 270, 295, 322, 362, -1, 381, -1, -1, -1, 404, 420, 461, 484]

    assert process_packages(7, 25, [[0, 21], [10, 35], [10, 12], [21, 13], [35, 11],
                            [35, 14], [51, 49], [59, 33], [59, 43], [67, 42],
                            [80, 14], [93, 45], [93, 38], [100, 8], [101, 31],
                            [108, 46], [123, 22], [127, 20], [139, 7],
                            [142, 43], [142, 12], [142, 25], [154, 25],
                            [154, 5], [154, 42]]) == [0, 21, 56, 68, 81, 92, 106, 155, 188, -1, 231, 245, 290, -1, -1, 328, -1, -1, -1, -1, -1, -1, -1, -1, -1]


if __name__ == "__main__":
    main()
    #test()
