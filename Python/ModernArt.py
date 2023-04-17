class Color:
    def __init__(self, num):
        self.num = num
        self.x1 = 11
        self.x2 = -1
        self.y1 = 11
        self.y2 = -1
import sys
sys.stdin = open("art.in")
sys.stdout = open("art.out", "w")
n = int(input())
canvas = []
for i in range(n):
    canvas.append(list(map(int, [*input()])))
nums = set()
visible = []
for r in canvas:
    for c in r:
        if (c not in nums and c != 0):
            nums.add(c)
            visible.append(Color(c))
for thing in visible:
    for j in range(n):
        for k in range(n):
            if (thing.num == canvas[j][k]):
                thing.x1 = j if j < thing.x1 else thing.x1
                thing.x2 = j if j > thing.x2 else thing.x2
                thing.y1 = k if k < thing.y1 else thing.y1
                thing.y2 = k if k > thing.y2 else thing.y2
for thing in visible:
    intruders = set()
    for i in range(thing.x1, thing.x2+1):
        for j in range(thing.y1, thing.y2+1):
            if canvas[i][j] != thing.num:
                intruders.add(canvas[i][j])
    nums -= intruders
print(len(nums))