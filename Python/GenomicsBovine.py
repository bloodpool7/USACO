import sys
sys.stdin = open("cownomics.in")
sys.stdout = open("cownomics.out", "w")
n, m = tuple(map(int, input().split()))
genomes = []
for i in range(2 * n):
    genomes.append(input())
possible = 0
for i in range(m):
    for j in range(i+1, m):
        for k in range(j + 1, m):
            spotty = set()
            plain = set()
            for a in range(n):
                spotty.add(genomes[a][i] + genomes[a][j] + genomes[a][k])
            for b in range(n, 2*n):
                plain.add(genomes[b][i] + genomes[b][j] + genomes[b][k])
            if (len(spotty.union(plain)) == len(spotty) + len(plain)):
                possible += 1
print(possible)