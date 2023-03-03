n, k = tuple(map(int, input().split()))
days = list(map(int, input().split()))
subs = [[days[0], 1]]
for i in range(1, n):
    join = (days[i] - days[i-1]) + subs[-1][1] + k 
    nojoin = subs[-1][1] + k + 1 + k 
    if join <= nojoin:
        subs[-1][1] += (days[i] - days[i-1])
    else:
        subs.append([days[i], 1])
numks = len(subs)
dayscovered = 0
for sub in subs:
    dayscovered += sub[1]
print(dayscovered + numks * k)