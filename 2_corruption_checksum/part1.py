def solution(text):

    text = text.replace("\t", " ")
    
    total = 0
    for line in text.split("\n"):
        if len(line) == 0: continue
        nums = map(int, line.split(" "))
        total += max(nums) - min(nums)

    return total


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())
