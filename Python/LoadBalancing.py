import sys
# sys.stdin = open("balancing.in")
# sys.stdout = open("balancing.out", "w")
n = int(input())
locs = [0] * 1000
for i in range(n):
    locs[i] = tuple(map(int, input().split()))
    