import sys
sys.stdin = open("shell.in","r")
sys.stdout = open("shell.out","w")
n = int(input())
guesses = []
for i in range(n):
    guesses.append(tuple(map(int, input().split())))
max_ = 0
for i in range(3):
    pebbles = ["."] * 3
    pebbles[i] = "p"
    count = 0
    for i in range(len(guesses)):
        temp = pebbles[guesses[i][0]-1]
        pebbles[guesses[i][0]-1] = pebbles[guesses[i][1]-1]
        pebbles[guesses[i][1]-1] = temp
        if pebbles[guesses[i][2]-1] == "p":
            count += 1
    if count > max_:
        max_ = count
print(max_)