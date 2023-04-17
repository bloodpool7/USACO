f = open("photo.in", "r")
n = int(f.readline())
b = list(map(int, f.readline().split()))
x = 1
count = 1
while ( True):
    x = count
    solutions = []
    nums_added = set()
    solutions.append(count)
    for i in range(len(b)):
        if (b[i] - x) < 1 or (b[i] - x) > n:
            break
        elif (b[i] - x) not in nums_added:
            solutions.append(b[i] - x)
            nums_added.add(b[i]-x)
            x = solutions[-1]
        else:
            break
    
    if (len(solutions) == n):
        break 
    count += 1
f = open("photo.out", "w")
f.write(" ".join(map(str, solutions)))
