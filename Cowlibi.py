g, n = tuple(map(int, input().split()))
grazers = [tuple(map(int, input().split())) for i in range(g)]
alibis = [tuple(map(int, input().split())) for i in range(n)]
nums = 0
for alibi in alibis:
    for graze in grazers:
        if (alibi[2] > graze[2]):
            continue
        distance = ((abs(graze[0] - alibi[0]) ** 2)+ (abs(graze[1] - alibi[1]) ** 2)) ** 0.5
        print(distance)
        if (distance <= (graze[2] - alibi[2])):
            nums += 1
            break 
print(nums)