int(input())
n = list(map(int, input().split()))
n.sort()
minimum = n[0] 
maxTuition = 0
index = -1
for i in range(len(n)):
    if (n[i] > minimum):
        minimum = n[i]
        tuition = n[i] * (len(n) - i)
        if (tuition > maxTuition):
            maxTuition = tuition
            index = i
print(maxTuition, n[index])