def solve():
    n = int(input())
    cows = list(map(int, input().split()))
    count = 0
    for i in range(len(cows)):
        if cows[i] == 0:
            count += 1
    sum_ = sum(cows)
    if (sum_ == 0):
        print(0)
        return None
    max_ = max(cows)
    solutions = {}
    for i in range(n, 0, -1):
        if (sum_/i - int(sum_/i) == 0) and sum_/i >= max_:
            solutions[int(sum_/i)] = n - i
    for solution in solutions.keys():
        sum1 = 0
        found = True
        for i in range(len(cows)):
            sum1 += cows[i]
            if sum1 == solution:
                sum1 = 0
            if sum1 > solution:
                found = False
                break
        if found:
            print(solutions[solution])
            break
for i in range(int(input())):
    solve()