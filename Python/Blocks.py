from itertools import permutations
def solve_word(word, blocks):
    allwords = ["".join(x) for x in list(permutations(word))]
    for w in allwords:
        for block in blocks:
            for i in range(len(w)):
                if (w[i] in block):
                    w = [*w]
                    w.pop(i)
                    w = "".join(w)
                    break
        if len(w) == 0:
            print("YES")
            return None
    print("NO")
n = int(input())
blocks = [input() for i in range(4)]
words = [input() for i in range(n)]
for i in range(n):
    solve_word(words[i], blocks)