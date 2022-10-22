import sys
sys.stdin = open('1963_소수경로.txt')
input = sys.stdin.readline

num_max = 10000
x = int(10000**(1/2))
check = [True]*(num_max+1)

for i in range(2, x):
    if check[i] == True:
        for j in range(i+i, num_max, i):
            check[j] = False

t = int(input())
for test_case in range(1, t+1):
    n, m = input().strip().split()
    m = int(m)
    visited = [False] * (int(num_max)+1)
    for visit in range(1000):
        visited[visit] = True
    now = set([n])
    nxt = set()
    visited[int(n)] = True
    cnt = 0
    flag = True
    while flag:
        while now:
            s = now.pop()
            if int(s) == m:
                flag = False
                break
            s = list(s)
            for i in range(4):
                temp = s[i]
                for j in range(10):
                    s[i] = str(j)
                    t = ''.join(s)
                    result = int(t)
                    if check[result] and not visited[result]:
                        visited[result] = True
                        nxt.add(t)
                s[i] = temp
        now, nxt = nxt, now
        cnt += 1
        if not now:
            break
    print(cnt-1)