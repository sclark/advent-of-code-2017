DIR_PAIRS = [("n", "s"),
             ("ne", "sw"),
             ("se", "nw")]

DIR_REDUCE = [("n", "se", "ne"),
              ("n", "sw", "nw"),
              ("ne", "s", "se"),
              ("ne", "nw", "n"),
              ("nw", "s", "sw"),
              ("sw", "se", "s")]


def steps_away(dirs):

    removed = True

    while removed:

        removed = False

        for (x, y) in DIR_PAIRS:

            if x in dirs and y in dirs:

                x_count = dirs.count(x)
                y_count = dirs.count(y)

                for _ in range(min(x_count, y_count)):
                    dirs.remove(x)
                    dirs.remove(y)

                removed = True

        for (x, y, z) in DIR_REDUCE:

            if x in dirs and y in dirs:

                x_count = dirs.count(x)
                y_count = dirs.count(y)

                min_count = min(x_count, y_count)
                for _ in range(min_count):
                    dirs.remove(x)
                    dirs.remove(y)

                dirs += ([z] * min_count)
                removed = True

    return dirs


def solution(dirs):

    dirs = dirs.split(",")
    dirs_reduced = []

    max_steps_away = 0

    for i in range(len(dirs)):

        dirs_reduced.append(dirs[i])
        dirs_reduced = steps_away(dirs_reduced)
        max_steps_away = max(max_steps_away, len(dirs_reduced))

    return max_steps_away


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())