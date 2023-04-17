t = int(input())
input()
for i in range(t):
    n, m = tuple(map(int, input().split()))
    b = []
    a = []
    for x in range(m):
        temp = input().split()
        a.append(int(temp[1]))
        b.append(list(map(int, [*temp[0]])))
    
    isLie = True
    rulesfound = []
    for j in range(len(b[0])):
        zeros = []
        ones = []
        for k in range(len(b)):
            if b[k][j] == 0:
                zeros.append(k)
            else:
                ones.append(k)
        
        values0 = [a[x] for x in zeros]
        values1 = [a[x] for x in ones]  

        if len(values0) > 0:
            x = values0[0]
            made = True
            for thing in values0:
                if thing != x:
                    made = False
                    break
            if made:
                for thing in zeros:
                    if thing not in rulesfound:
                        rulesfound.append(thing)
        if len(values1) > 0:
            x = values1[0]
            made = True
            for thing in values1:
                if thing != x: 
                    made = False
                    break
            if made:
                 for thing in ones:
                    if thing not in rulesfound:
                        rulesfound.append(thing)
    
    if (len(rulesfound) >= len(b) - 1):
        isLie = False
    if (isLie):
        print("LIE")
    else:
        print("OK")
    if(i != t-1):
        input()