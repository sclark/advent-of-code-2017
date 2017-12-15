FACTOR_A = 16807
FACTOR_B = 48271
MAX_VAL = 2147483647

def gen_next():

    global val_a
    global val_b

    val_a = (val_a * FACTOR_A) % MAX_VAL
    val_b = (val_b * FACTOR_B) % MAX_VAL


def lower_16(x):

    x = bin(x)[2:]
    x = x[-16:]
    x = ("0" * (16-len(x))) + x

    return x


def solution(text):

    global val_a
    global val_b

    val_a, val_b = text.split("\n")
    val_a = int(val_a.split(" ")[-1])
    val_b = int(val_b.split(" ")[-1])
    gen_next()

    total = 0

    for _ in range(40000000):

        if lower_16(val_a) == lower_16(val_b):
            total += 1

        gen_next()

    return total


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())