f = open("breedflip.in")
n = int(f.readline())
a = f.readline()
b = f.readline()
flip = False
flipcount = 0
for i in range(n):
    if b[i] != a[i] and not flip:
        flip = True
        flipcount += 1
    elif b[i] == a[i] and flip:
        flip = False
f = open("breedflip.out", "w")
f.write(str(flipcount))