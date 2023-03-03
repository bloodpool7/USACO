f = open("milkorder.in", "r")
n, m, k = tuple(map(int, f.readline().split()))
order = list(map(int, f.readline().split()))
demands = []
for i in range(k):
    demands.append(tuple(map(int, f.readline().split())))
f = open("milkorder.out", "w")
demands = [(x, y-1) for x,y in demands]
solution = [None] * (n+1)
bypass = False
count = 0
for i in range(len(demands)):
    solution[demands[i][1]] = demands[i][0]
    if demands[i][0] in order:
        count += 1

x = 1
for i in range(1000000):
    x+=i

print(solution)

if 1 not in order:
    startingidx = len(solution) - 1
    for i in range(len(order) - 1, -1, -1):
        if order[i] not in solution:
            idx = startingidx
            placed = False
            while(not placed):
                if(solution[idx] == None):
                    solution[idx] = order[i]
                    placed = True
                else:
                    idx -= 1
        else:
            startingidx = solution.index(order[i]) - 1
else:
    startingidx = 0
    for i in range(len(order)):
        if order[i] not in solution:
            idx = startingidx
            placed = False
            while(not placed):
                if(solution[idx] == None):
                    solution[idx] = order[i]
                    placed = True
                else:
                    idx += 1
        else:
            startingidx = solution.index(order[i]) + 1
    f.write(str(solution.index(1)+1))
    bypass = True

print(solution)

if(not bypass):
    answer = -1
    for i in range(len(solution)):
        if (solution[i] == None):
            answer = i
            break


    f.write(str(answer+1))