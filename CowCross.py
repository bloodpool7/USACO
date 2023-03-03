import sys
sys.stdin = open("circlecross.in")
sys.stdout = open("circlecross.out", "w")
log = input()
log_reverse = ""
for i in range(51, -1, -1):
    log_reverse += log[i]
pairs = 0
for i in range(26):
    for j in range(i+1, 26):
        chr1 = chr(i + 65)
        chr2 = chr(j + 65)
        idx1 = log.index(chr1)
        idx2 = log.index(chr2)
        idx1rev = 51 - log_reverse.index(chr1)
        idx2rev = 51 - log_reverse.index(chr2)
        if idx1 < idx2:
            if idx1rev > idx2 and idx1rev < idx2rev:
                pairs += 1
        elif idx1 > idx2:
            if idx1rev > idx2rev and idx1 < idx2rev:
                pairs += 1
print(pairs)
