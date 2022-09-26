import sys
from collections import deque
sys.stdin = open('1966_프린터큐.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    lst = [*map(int, input().split())]
    q = deque()
    for i in range(len(lst)):
        q.append((lst[i], i))
    cnt = 0
    while q:
        x = max(q)
        y = q.popleft()
        if y[0] == x[0]:
            cnt += 1
            if y[1] == m:
                print(cnt)
                break
        else:
            q.append(y)