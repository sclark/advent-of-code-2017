def solution(lines):

    regs = {}

    lines = lines.split("\n")

    for line in lines:
        reg, op, val, if_const, cond_reg, cond_op, cond_val = line.split(" ")

        val = int(val)
        cond_val = int(cond_val)

        if reg not in regs:
            regs[reg] = 0
        if cond_reg not in regs:
            regs[cond_reg] = 0

        cond = False
        if cond_op == ">":
            cond = regs[cond_reg] > cond_val
        elif cond_op == "<":
            cond = regs[cond_reg] < cond_val
        elif cond_op == ">=":
            cond = regs[cond_reg] >= cond_val
        elif cond_op == "<=":
            cond = regs[cond_reg] <= cond_val
        elif cond_op == "==":
            cond = regs[cond_reg] == cond_val
        elif cond_op == "!=":
            cond = regs[cond_reg] != cond_val
        else:
            return None

        if cond:
            if op == "inc":
                regs[reg] += val
            elif op == "dec":
                regs[reg] -= val
            else:
                return None

    return regs[max(regs, key=regs.get)]


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())