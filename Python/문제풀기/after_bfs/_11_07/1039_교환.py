import sys
sys.stdin = open('1039_교환.txt')
input = sys.stdin.readline

n, k = input().strip().split()
m = len(str(n))

now = set([n])
nxt = set()
if int(n) >= 10:
    for x in range(int(k)):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(m-1):
                for j in range(i+1, m):
                    s[i], s[j] = s[j], s[i]
                    if s[0] == '0':
                        pass
                    else:
                        nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now
    if len(now):
        print(max(map(int, now)))
    else:
        print(-1)
else:
    print(-1)