import sys
sys.stdin = open("sleepy.in")
sys.stdout = open("sleepy.out", "w")
n = int(input())
cows = list(map(int, input().split()))
last_instance = -1
for i in range(n-1):
    if (cows[i] > cows[i+1]):
        last_instance = i
print(last_instance + 1)