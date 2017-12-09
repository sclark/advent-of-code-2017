def solution(text):

    garbage_sum = 0

    group_stack = []

    skip = False
    garbage = False

    for c in text:

        if skip:
            skip = False

        elif c == "!":
            skip = True

        elif garbage:
            garbage = not (c == ">")
            if garbage:
                garbage_sum += 1

        elif c == "<":
            garbage = True

        elif c == "{":
            if len(group_stack) == 0:
                group_stack.append(1)
            else:
                group_stack.append(group_stack[-1]+1)

        elif c == "}":
            group_stack.pop()

    return garbage_sum


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())