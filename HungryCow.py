n, t = tuple(map(int, input().split()))
days = [tuple(map(int, input().split())) for i in range(n)]
stock = 0
eaten = 0
for i in range(n-1):
    if stock + days[i][1] < days[i+1][0] - days[i][0]:
        eaten += days[i][1] + stock
        stock = 0
    elif stock + days[i][1] > days[i+1][1] - days[i][0]:
        eaten += days[i+1][0] - days[i][0] 
        stock += days[i][1] - (days[i+1][0] - days[i][0]) 
if stock + days[-1][1] <= t - days[-1][0]:
    eaten += days[-1][1] + stock 
elif stock + days[-1][1] > t - days[-1][0]:
    eaten += t - days[-1][0] + 1
print(eaten)