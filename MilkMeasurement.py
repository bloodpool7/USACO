import sys
sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")
board = {"Bessie" : 7, "Mildred" : 7, "Elsie": 7}
n = int(input())
updates = []
for i in range(n):
    updates.append(tuple(input().split()))
updates = [(int(x), y, z) for x,y,z in updates]
updates.sort()
top = ["Bessie", "Mildred", "Elsie"]
oldTop = ["Bessie", "Mildred", "Elsie"]
changes = 0
for i in range(len(updates)):
    if updates[i][2][0] == "+":
        board[updates[i][1]] += int(updates[i][2][1])
    else:
        board[updates[i][1]] -= int(updates[i][2][1])
    max_ = max(board.values())
    top = []
    if board["Bessie"] == max_:
        top.append("Bessie")
    if board["Mildred"] == max_:
        top.append("Mildred")
    if board["Elsie"] == max_:
        top.append("Elsie")
    if len(top) != len(oldTop) or top[0] != oldTop[0]:
        changes += 1
    oldTop = top
print(changes)