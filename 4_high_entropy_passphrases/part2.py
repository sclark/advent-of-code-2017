def is_anagram(s1, s2):

    s1 = list(s1)
    s1.sort()
    s2 = list(s2)
    s2.sort()

    return s1 == s2


def solution(phrases):

    total = 0

    for phrase in phrases.split("\n"):

        phrase = phrase.strip().split(" ")

        valid = True
        for i in range(len(phrase)):
            for j in range(len(phrase)):
                if i != j:

                    if is_anagram(phrase[i], phrase[j]):
                        valid = False
                        break

            if not valid:
                break

        if valid:
            total += 1

    return total


if __name__ == "__main__":

    with open("input.txt", "rt") as f:
        print solution(f.read().strip())