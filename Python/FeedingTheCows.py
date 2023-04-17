import concurrent.futures
import multiprocessing
def solve():
    n, k = tuple(map(int, input().split()))
    s = input()

    solution = ["."]*n
    gcovered = -1
    hcovered = -1
    for i,c in enumerate(s):
        if c == "G" and i > gcovered:
            if (i + k) < len(s):
                if (solution[i+k] == "."):
                    solution[i+k] = "G"
                    gcovered = i+2*k
                else:
                    solution[i+k-1] = "G"
                    gcovered = (i-1)+2*k
            else:
                if (solution[-1] == "."):
                    solution[-1] = "G"
                else:
                    solution[-2] = "G"
                gcovered = n
        elif c == "H" and i > hcovered:
            if (i + k) < len(s):
                if (solution[i+k] == "."):
                    solution[i+k] = "H"
                    hcovered = i+2*k
                else:
                    solution[i+k-1] = "H"
                    hcovered = (i-1)+2*k
            else:
                if (solution[-1] == "."):
                    solution[-1] = "H"
                else:
                    solution[-2] = "H"
                hcovered = n
    print(n-solution.count("."))
    print("".join(solution))

for i in range(int(input())):
    solve()
