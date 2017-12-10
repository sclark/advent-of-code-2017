KEY_LEN = 256
SUB_KEY_LEN = 16
ROUNDS = 64
MAGIC_LENGTHS = [17, 31, 73, 47, 23]

def do_reverse(L, start, length):

    stop = start + (length - 1)

    while start <= stop:

        temp = L[start % len(L)]
        L[start % len(L)] = L[stop % len(L)]
        L[stop % len(L)] = temp

        start += 1
        stop -= 1

    return L


def solution(chars):

    L = [ x for x in range(KEY_LEN) ]
    pos = 0
    skip = 0

    chars = list(chars)
    lengths = map(ord, chars)
    lengths += MAGIC_LENGTHS

    for length in (lengths * ROUNDS):

        L = do_reverse(L, pos, length)
        pos = (pos + length + skip) % len(L)
        skip += 1

    L_dense = []
    for i in range(0, KEY_LEN, SUB_KEY_LEN):

        result = None
        for x in L[i:i+SUB_KEY_LEN]:
            if result == None:
                result = x
            else:
                result = result ^ x

        L_dense.append(format(result, 'x'))

    return "".join(L_dense)


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())