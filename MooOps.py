works = {"OOO":1, "MOO":0, "MOM":1, "OOM":2, "OMO":None, "OMM":None, "MMM":None, "MMO":None}
def solve():
    nums = {"OOO":0, "MOO":0, "MOM":0, "OOM":0}
    s = input()
    for i in range(len(s)-2):
        x = works[s[i:i+3]]
        if x != None:
            nums[s[i:i+3]] += 1
    count = 0
    if nums["MOO"] > 0:
        pass
    elif nums["OOO"] > 0:
        count = 1
    elif nums["MOM"] > 0:
        count = 1
    elif nums["OOM"] > 0:
        count = 2
    else:
        print(-1)
        return None
    print(count + len(s) - 3)
for i in range(int(input())):
    solve()