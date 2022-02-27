def find_pattern_in_text(pattern, text):

    # fix a large prime
    p = 1000000007

    # output: Indexes of occurrences of a string
    # Pattern to string Text in ascending order
    output = []

    size_pattern = len(pattern)

    # get pattern hash
    hash_pattern = 0
    for ch in pattern:
        hash_pattern = (hash_pattern + ord(ch)) % p

    # get the hash of the current part of the text and compare it with the pattern hash
    hash_text = 0
    for i in range(len(text)):

        # add the next character to the right to the hash and remove the previous character from the left
        prev_ch_code = ord(text[i - size_pattern]) if (i - size_pattern) >= 0 else 0
        next_ch_code = ord(text[i])
        hash_text = (hash_text + next_ch_code - prev_ch_code) % p

        # if the hashes match
        if i >= (size_pattern - 1) and hash_text == hash_pattern:

            # compare strings character by character
            if pattern == text[i - size_pattern + 1: i + 1]:
                output.append(i - size_pattern + 1)

    return " ".join(map(str, output))


def main():

    # read pattern and text
    pattern, text = input(), input()

    print(find_pattern_in_text(pattern, text))


def test():
    assert find_pattern_in_text('aba', 'abacaba') == '0 4'
    assert find_pattern_in_text('Test', 'testTesttesT') == '4'
    assert find_pattern_in_text('aaaaa', 'baaaaaaa') == '1 2 3'


if __name__ == "__main__":
    main()