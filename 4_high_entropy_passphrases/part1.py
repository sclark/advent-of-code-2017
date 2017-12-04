def solution(phrases):

    total = 0

    for phrase in phrases.split("\n"):

        phrase = phrase.strip().split(" ")

        valid = True
        seen = set()
        for word in phrase:
            if word in seen:
                valid = False
                break
            seen.add(word)

        if valid:
            total += 1

    return total


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())