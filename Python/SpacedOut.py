def transpose(matrix):
    output = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        output.append(row)
    return output
n = int(input())
canvas = []
for i in range(n):
    canvas.append(list(map(int, input().split())))
canvasT = transpose(canvas)
rowSum = 0
colSum = 0
for i in range(len(canvas)):
    x = sum(canvas[i][::2])
    y = sum(canvas[i][1::2])
    rowSum += (x if x > y else y)
    x = sum(canvasT[i][::2])
    y = sum(canvasT[i][1::2])
    colSum += (x if x > y else y)
print(colSum if colSum > rowSum else rowSum)