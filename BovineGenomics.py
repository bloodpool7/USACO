import sys
sys.stdin = open("cownomics.in")
sys.stdout = open("cownomics.out", "w")
n, m = tuple(map(int, input().split()))
cows = []
for i in range(2*n):
    cows.append(input())
possible = 0
for i in range(m):
    spotty = set()
    plain = set()
    for j in range(n):
        spotty.add(cows[j][i])
    for j in range(n, 2*n):
        plain.add(cows[j][i])
    if len(spotty.union(plain)) == len(spotty) + len(plain):
        possible += 1
print(possible)