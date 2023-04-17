x, y = tuple(map(int, input().split()))
x2 = bin(x)[2:]

if(len(x2) < 63):
    for i in range(63 - len(x2)):
        x2 = "0" + x2

if(x2[-y] == "0"):
    print(x + 2**(y-1))
else:
    print(x - 2**(y-1))
