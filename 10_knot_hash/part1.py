def do_reverse(L, start, length):

    stop = start + (length - 1)

    while start <= stop:

        temp = L[start % len(L)]
        L[start % len(L)] = L[stop % len(L)]
        L[stop % len(L)] = temp

        start += 1
        stop -= 1

    return L


def solution(lengths):

    L = [ x for x in range(256) ]
    pos = 0
    skip = 0

    lengths = lengths.split(",")
    lengths = map(int, lengths)

    for length in lengths:

        L = do_reverse(L, pos, length)
        pos = (pos + length + skip) % len(L)
        skip += 1

    return L[0] * L[1]


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())