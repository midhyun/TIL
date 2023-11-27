import sys
input = sys.stdin.readline

N = int(input())
init = ''
for _ in range(N):
    init += input().strip()

s, e = 0, N-1
tmp = ''
cnt = 0
while s != e:
    if init[s] > init[e]:
        tmp += init[e]
        e -= 1
    elif init[s] < init[e]:
        tmp += init[s]
        s += 1
    elif init[s] == init[e]:
        ts, te = s, e
        diff = False
        while ts <= te:
            ts += 1; te -= 1
            if init[ts] == init[te]:
                pass
            elif init[ts] > init[te]:
                tmp += init[e]
                e -= 1
                diff = True
                break
            elif init[ts] < init[te]:
                tmp += init[s]
                s += 1
                diff = True
                break
        if not diff:
            tmp += init[s]
            s += 1
    cnt += 1
    if cnt % 80 == 0:
        tmp += '\n'
tmp += init[s]

print(tmp)
