def solution(nums):

    nums = nums.split(" ")
    nums = map(int, filter(lambda x: len(x) > 0, nums))

    seen = {}

    steps = 0

    while tuple(nums) not in seen:

        seen[tuple(nums)] = steps

        blocks = max(nums)
        i = nums.index(blocks)

        # Redistribute
        nums[i] = 0
        while blocks > 0:
            i += 1
            nums[i % len(nums)] += 1
            blocks -= 1

        steps += 1

    return steps - seen[tuple(nums)]


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())