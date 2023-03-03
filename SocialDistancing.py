import math
import sys
sys.stdin = open("socdist.in")
sys.stdout = open("socdist.out", "w")
def check(dist, ranges, n):
    r = 0
    idx = 0
    while n > 0:
        if r == len(ranges):
            return False
        if (idx < ranges[r][0]):
            idx = ranges[r][0]
            continue
        elif(idx > ranges[r][1]):
            r += 1
            continue
        else:
            n -= 1
            idx += dist
    return True
n, m = tuple(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for x in range(m)]
ranges.sort()
low = ranges[0][0]
high = ranges[-1][-1]
hlast = False
llast = False
while low <= high:
    mid = math.floor((low + high) / 2)
    if (check(mid, ranges, n)):
        low = mid + 1
        llast = True
        hlast = False
    else:
        high = mid - 1
        hlast = True
        llast = False
print(mid + 1 if llast else mid -1)