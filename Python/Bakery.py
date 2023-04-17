# import sys
# sys.stdin = open("bakery.in")
def findlowestmultiple(base, num):
    num -= num % base 
    return int(num / base)
def solve():
    n, ctime, mtime = tuple(map(int, input().split()))
    orders = [list(map(int, input().split())) for i in range(n)]
    money = 0
    for i in range(n):
        expensive = 0
        hr = 0
        for i in range(len(orders)):
            rate = (orders[i][0] * ctime + orders[i][1] * mtime) / orders[i][2]
            hr = rate if rate > hr else hr
            expensive = i if hr == rate else expensive
        cookie = False
        stingy = orders[expensive]
        if stingy[0] >= stingy[1]:
            cookie = True
        else:
            cookie = False
        if cookie:
            if (stingy[0] * ctime + stingy[1] * mtime <= stingy[2]):
                continue
            if stingy[1] * mtime >= stingy[2]:
                money += ctime - 1
                ctime = 1
                stingy[2] -= stingy[0]
                newval = findlowestmultiple(stingy[1], stingy[2])
                money += mtime - newval
                mtime = newval
            else:
                newval = findlowestmultiple(stingy[0], stingy[2]- mtime * stingy[1])
                money += ctime - newval
                ctime = newval
                stingy[2] -= ctime * stingy[0]
                if (mtime * stingy[1] > stingy[2]):
                    newval = findlowestmultiple(stingy[1], stingy[2])
                    money += mtime - newval
                    mtime = newval
        else:
            if (stingy[0] * ctime + stingy[1] * mtime <= stingy[2]):
                continue
            if stingy[0] * mtime >= stingy[2]:
                money += ctime - 1
                ctime = 1
                stingy[2] -= stingy[1]
                newval = findlowestmultiple(stingy[0], stingy[2])
                money += mtime - newval
                mtime = newval
            else:
                newval = findlowestmultiple(stingy[1], stingy[2]- mtime * stingy[0])
                money += ctime - newval
                ctime = newval
                stingy[2] -= ctime * stingy[1]
                if (mtime * stingy[0] > stingy[2]):
                    newval = findlowestmultiple(stingy[0], stingy[2])
                    money += mtime - newval
                    mtime = newval
        orders.pop(expensive)
    print(money)
for i in range(int(input())):
    input()
    solve()