import sys
sys.stdin = open("tracing.in")
sys.stdout = open("tracing.out", "w")
n, t = tuple(map(int, input().split()))
cows = input()
log = [""] * t
valid0s = 0
validKs = []
for i in range(t):
    log[i] = tuple(map(int, input().split()))
log.sort()
for i in range(n):
    if (cows[i] != "1"):
        continue
    else:
        works = False
        for k in range(t+1):
            iteration = list(("0" * n))
            iteration[i] = "1"
            ks = dict(zip(range(n), [0] * n))
            for j in range(t):
                meet = log[j]
                if iteration[meet[1] - 1] == "1":
                    ks[meet[1] - 1] += 1
                if iteration[meet[2] - 1] == "1":
                    ks[meet[2] - 1] += 1
                if iteration[meet[1] - 1] == "1" and ks[meet[1] - 1] <= k:
                    iteration[meet[2] - 1] = "1"
                if iteration[meet[2] - 1] == "1" and ks[meet[2] - 1] <= k:
                    iteration[meet[1] - 1] = "1"
            iteration = "".join(iteration)
            if (iteration == cows):
                validKs.append(k)
                works = True
        if (works):
            valid0s += 1
validKs.sort()
print(valid0s, validKs[0], ("Infinity" if validKs[-1] == t else validKs[-1]))