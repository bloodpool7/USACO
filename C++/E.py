x = int(input())
count = 0
for i in range(-x, x+1, 1):
    for j in range(-x, x+1, 1):
        for k in range(-x, x+1, 1):
            if ((i * i) + (j * j) + (k * k ) <= x * x):
                count += 1
print(count)