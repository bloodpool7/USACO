import sys
sys.stdin = open("outofplace.in","r")
sys.stdout = open("outofplace.out","w")
n = int(input())
cows = []
for i in range(n):
    cows.append(int(input()))
cow = 0
idx = 0
for i in range(0, n):
    if i != 0 and cows[i] < cows[i-1]:
        cow = cows[i]
        idx = i
        swaps = 0
        for j in range(idx, 0, -1):
            if (cows[j-1] > cow):
                if cows[j-1] == cows[j]:
                    continue
                else:
                    swaps+=1
                    cows[idx] = cows[j]
                    cows[j] = cows[idx]
                    idx = j
    elif i != n-1 and cows[i] > cows[i+1]:
        cow = cows[i]
        idx = i
        swaps = 0
        for j in range(idx, n-1):
            if (cows[j+1] < cow):
                if cows[j+1] == cows[j]:
                    continue
                else:
                    swaps+=1
                    cows[idx] = cows[j]
                    cows[j] = cows[idx]
                    idx = j

print(swaps)
