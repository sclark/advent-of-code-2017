def solution(jumps):

    jumps = jumps.split("\n")
    jumps = map(int, jumps)

    curr = 0
    steps = 0

    while 0 <= curr < len(jumps):

        next = curr + jumps[curr]
        jumps[curr] += 1
        curr = next

        steps += 1

    return steps


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())