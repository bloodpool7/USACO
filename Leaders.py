from math import *
n = int(input())
c = input()
e = [x-1 for x in list(map(int, input().split()))]
firstG = n
firstH = n
lastG = -1 
lastH = -1
for i, s in enumerate(c):
    if i < firstG and s == "G":
        firstG = i
    elif i < firstH and s == "H":
        firstH = i
    if i > lastG and s == "G":
        lastG = i
    elif i > lastH and s == "H":
        lastH = i
allLocs = []
for i in range(max(firstG, firstH) + 1):
    if c[i] == "G":
        if i <= firstG and e[i] >= lastG:
            allLocs.append(i)
    elif c[i] == "H":
        if i <= firstH and e[i] >= lastH:
            allLocs.append(i)
count = 0
for i in range(allLocs[-1]):
    for j in range(len(allLocs)):
        if e[i] >= allLocs[j] and i < allLocs[j]:
            count += 1
disregard = 0
for i in range(len(allLocs)):
    for j in range(len(allLocs)):
        if e[allLocs[i]] > allLocs[j] and allLocs[i] < allLocs[j]:
            disregard += 1
permutation = int(factorial(len(allLocs))/(2 * factorial(len(allLocs)-2))) if (len(allLocs)) >= 2 else 0
print(count + permutation - disregard)