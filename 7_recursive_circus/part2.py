def get_tree_weight(node, nodes):

    tree_weights = []

    balanced = True
    balanced_weight = 0

    (weight, children) = nodes[node]
    for child in children:

        child_tree_weight = get_tree_weight(child, nodes)
        (child_weight, _) = nodes[child]

        if balanced_weight == 0:
            balanced_weight = child_tree_weight

        if balanced_weight != child_tree_weight:
            balanced = False

        tree_weights.append( (child_tree_weight, child_weight) )

    if not balanced:
        print tree_weights

    return weight + sum(x[0] for x in tree_weights)


def solution(lines):

    nodes = {}
    all_children = []

    lines = lines.split("\n")
    for line in lines:

        name = line[:line.find(" ")]
        weight = int(line[line.find("(")+1:line.find(")")])
        children = []

        delim = "->"
        if delim in line:
            children = line[line.find(delim) + len(delim):].strip()
            children = children.split(", ")

        nodes[name] = (weight, children)
        all_children += children

    root = list(set(nodes.keys()) - set(all_children))[0]

    get_tree_weight(root, nodes)



if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())