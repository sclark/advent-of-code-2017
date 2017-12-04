def solution(text):

    text = text.replace("\t", " ")
    
    total = 0
    for line in text.split("\n"):
        if len(line) == 0: continue
        nums = map(int, line.split(" "))
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] % nums[j] == 0:
                    total += (nums[i] / nums[j])

    return total


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())
