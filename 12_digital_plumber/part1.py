def build_pipes(text):

    pipes = {}

    for line in text.split("\n"):
        key, children = line.split("<->")
        key = int(key)
        children = map(int, children.split(","))

        pipes[key] = children

    return pipes


def solution(text):

    pipes = build_pipes(text)

    closed = []
    frontier = [0]

    while len(frontier) != 0:

        curr = frontier.pop(0)

        for child in pipes[curr]:

            if child not in closed:
                closed.append(child)
                frontier.append(child)

    return len(closed)


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())