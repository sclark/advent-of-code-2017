def check_firewall(scanners, t):

    for key in scanners:

        if (key+t) % (2*(scanners[key]-1)) == 0:

            return False

    return True

def solution(text):

    delay = 0
    scanners = {}

    for line in text.split("\n"):

        pos, length = line.split(":")
        pos = int(pos)
        length = int(length)

        scanners[pos] = length

    while True:

        if check_firewall(scanners, delay):
            return delay

        delay += 1

    return None


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())