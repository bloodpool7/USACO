def check_validity(solution, limit, ranges):
    for i in range(limit+1):
        for j in range(len(ranges[i])):
            test = solution[i:j+1+i]
            if max(test) - min(test) != ranges[i][j]:
                return False
    return True
def ok(num, ranges):
    indices = []
    for i in range(len(ranges)):
        if max(num[:i+1]) - min(num[:i+1]) != ranges[i]:
            indices.append(i)
    return indices
n = int(input())
ranges = []
for i in range(n):
    ranges.append(list(map(int, input().split())))
solution = ranges[0]
for i in range(n):
    test = solution[i:]
    indices = ok(test, ranges[i])
    ma = max(test)
    mi = min(test)
    for index in indices:
        options = [test[index-1] + (ranges[i][index] - ranges[i][index-1]), test[index-1] - (ranges[i][index] - ranges[i][index-1])]
        test2 = list(solution)
        test3 = list(solution)
        test2[index + i] = options[0]
        test3[index + i] = options[1]
        if check_validity(test2, i-1, ranges):
            solution[index + i] = options[0]
        if check_validity(test3, i-1, ranges):
            solution[index + i] = options[1] 
print(" ".join(list(map(str, solution))))