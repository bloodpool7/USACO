import sys
sys.stdin = open("maxcross.in")
sys.stdout = open("maxcross.out", "w")
n, k, b = tuple(map(int, input().split()))
cows = [0] * n
for i in range(b):
    cows[int(input()) - 1] = 1
minones = n
for i in range(n-k+1):
    count = cows[i:i+k].count(1)
    if count < minones:
        minones = count
print(minones)