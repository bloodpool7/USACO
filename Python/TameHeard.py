import sys
sys.stdin = open("taming.in")
sys.stdout = open("taming.out", "w")
n = int(input())
log = list(map(int, input().split()))
log[0] = 0
possible = True
for i in range(1, n):
    if log[i] != -1:
        for j in range(i-log[i], i):
            if log[j] == -1 or log[j] == j - (i-log[i]):
                log[j] = j - (i-log[i])
            else:
                possible = False
                break
    if not possible:
        break
if possible:
    print(log.count(0), log.count(0) + log.count(-1))
else:
    print(-1)