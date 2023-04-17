# import sys
# sys.stdin = open("grid.in")
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
def solve():
    n = int(input())
    desired = [[*input()] for x in range(n)]
    k = int(input())
    stamp = [[*input()] for x in range(k)]
    canvas = []
    for i in range(n):
        canvas.append(["."] * n)
    for m in range(4):
        for i in range(n-k+1):
            for j in range(n-k+1):
                worksHere = True
                for x in range(i, i+k):
                    for y in range(j, j+k):
                        if stamp[x-i][y-j] == "*" and desired[x][y] == ".":
                            worksHere = False
                            break
                    if not worksHere:
                        break
                if worksHere:
                    for x in range(i, i+k):
                        for y in range(j, j+k):
                            if stamp[x-i][y-j] == "*":
                                canvas[x][y] = "*"  
        stamp = rotate(stamp)
    completed = True
    for i in range(n):
        for j in range(n):
            if canvas[i][j] != desired[i][j]:
                completed = False     
    if not completed:
        print("NO")
    else:
        print("YES")
for i in range(int(input())):
    input()
    solve()