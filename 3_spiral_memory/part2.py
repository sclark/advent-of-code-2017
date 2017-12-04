table = {(0,0): 1}

def set(x, y):

    val = 0
    for i in range(-1,1+1):
        for j in range(-1,1+1):
            val += get(x+i, y+j)

    table[(x, y)] = val

    return val


def get(x, y):

    if (x, y) not in table:
        return 0
    return table[(x, y)]



def build_table(limit):

    (x, y) = (1, 0)
    ring = 3
    steps = 0

    while True:

        num = set(x, y)

        if num > limit:
            return num

        # Not proud of this piece of code either
        if steps < ring - 2:
            (x, y) = (x, y+1)
        elif steps < ring * 2 - 3:
            (x, y) = (x-1, y)
        elif steps < ring * 3 - 4:
            (x, y) = (x, y-1)
        elif steps < ring * 4 - 5:
            (x, y) = (x+1, y)
        else:
            (x, y) = (x+1, y)
            ring += 2
            steps = -1

        steps += 1


def solution(num):

    return build_table(num)


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(int(f.read().strip()))