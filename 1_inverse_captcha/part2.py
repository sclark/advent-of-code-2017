def solution(captcha):

    total = 0
    chars = list(captcha)

    for i, c in enumerate(chars):
        
        if c == chars[(i+len(chars)/2) % len(chars)]:
            total += int(c)

    return total


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())
