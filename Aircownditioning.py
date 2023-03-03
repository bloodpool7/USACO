import math
n, m = tuple(map(int, input().split()))
cows = []
for i in range(n):
    cows.append(list(map(int, input().split())))
conditioners = []
for i in range(m):
    conditioners.append(list(map(int, input().split())))
best_cost = math.inf
for i in range(1, 2**m):
    binary = str(bin(i)[2:])
    binary = '0' * (m - len(binary)) + binary
    stalls = [0] * 101
    for cow in cows:
        for j in range(cow[0], cow[1] + 1):
            stalls[j] += cow[2]
    cost = 0
    for j in range(len(binary)):
        cond = conditioners[j]
        if binary[j] == "1":
            for k in range(cond[0], cond[1]+1):
                stalls[k] -= cond[2]
            cost += cond[3]
    go = False
    for thing in stalls:
        if thing > 0:
            go = True
            break
    if not go and cost < best_cost:
        best_cost = cost
print(best_cost)