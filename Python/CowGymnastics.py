import sys
sys.stdin = open("gymnastics.in")
sys.stdout = open("gymnastics.out", "w")
k, n = tuple(map(int, input().split()))
rankings = []
for i in range(k):
    rankings.append(list(map(int, input().split())))
pairs = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        idx1 = rankings[0].index(i)
        idx2 = rankings[0].index(j)
        correct = (idx1 - idx2) > 0
        broke = False
        for x in range(1, k):
            idx1 = rankings[x].index(i)
            idx2 = rankings[x].index(j)
            if ((idx1 - idx2) > 0) != correct:
                broke = True
                break
        if (not broke):
            pairs += 1
print(pairs)