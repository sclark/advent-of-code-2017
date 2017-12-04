def get_pos(num):
    
    import math

    ring = math.ceil(math.sqrt(num))
    ring += 1 - (ring % 2)

    cur = ring ** 2
    (x, y) = (int(ring / 2), -int(ring / 2))

    # Not proud of this piece of code
    steps = 0
    while cur - steps != num:

        if steps < ring - 1:
            (x, y) = (x-1, y)
        elif steps < ring * 2 - 2:
            (x, y) = (x, y+1)
        elif steps < ring * 3 - 3:
            (x, y) = (x+1, y)
        else:
            (x, y) = (x, y-1)

        steps += 1

    return (x, y)
    

def solution(num):

    (x, y) = get_pos(num)
    return abs(x) + abs(y)


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(int(f.read().strip()))