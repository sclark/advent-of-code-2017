def solution(lines):

    nodes = {}
    all_children = []

    lines = lines.split("\n")
    for line in lines:

        name = line[:line.find(" ")]
        children = []

        delim = "->"
        if delim in line:
            children = line[line.find(delim) + len(delim):].strip()
            children = children.split(", ")

        nodes[name] = children
        all_children += children

    return list(set(nodes.keys()) - set(all_children))[0]



if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())