def build_pipes(text):

    pipes = {}
    community = set()

    for line in text.split("\n"):

        key, children = line.split("<->")
        key = int(key)
        children = map(int, children.split(","))

        pipes[key] = children

        for x in children + [key]:
            if x not in community:
                community.add(x)

    return pipes, community


def solution(text):

    groups = 0
    closed = set()
    frontier = []

    pipes, community = build_pipes(text)

    while len(community - closed) > 0:

        frontier.append((community - closed).pop())
        groups += 1

        while len(frontier) != 0:

            curr = frontier.pop(0)
            closed.add(curr)

            for child in pipes[curr]:

                if child not in closed:
                    frontier.append(child)

    return groups


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())