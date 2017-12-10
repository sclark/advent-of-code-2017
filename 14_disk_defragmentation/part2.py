KEY_LEN = 256
SUB_KEY_LEN = 16
ROUNDS = 64
MAGIC_LENGTHS = [17, 31, 73, 47, 23]

GRID_SIZE = 128

def zero_prepend(s, l):

    while len(s) < l:
        s = "0" + s

    return s


def do_reverse(L, start, length):

    stop = start + (length - 1)

    while start <= stop:

        temp = L[start % len(L)]
        L[start % len(L)] = L[stop % len(L)]
        L[stop % len(L)] = temp

        start += 1
        stop -= 1

    return L


def knot_hash(chars):

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

        L_dense.append(zero_prepend(format(result, 'x'), 2))

    return "".join(L_dense)


def solution(hash_key):

    grid = []

    for i in range(GRID_SIZE):

        hash = knot_hash(hash_key + "-" + str(i))
        used_bits = bin(int(hash, 16))[2:]

        for j, bit in enumerate(used_bits):
            if bit == "1":
                grid.append((i,j))

    ranges = 0

    while len(grid) > 0:

        ranges += 1l

        queue = [ grid[0] ]

        while len(queue) > 0:

            (i,j) = queue.pop(0)

            if (i,j) in grid:
                grid.remove((i,j))
                queue += [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ]

    return ranges


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())


