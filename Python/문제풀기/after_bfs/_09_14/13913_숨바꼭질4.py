import sys
from collections import deque
sys.stdin = open('13913_숨바꼭질4.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100010
visited = [-1]*MAX

def bfs(n):
    q = deque()
    q.append((n, 0))
    visited[n] = True
    while q:
        x, t = q.popleft()
        if x == k:
            return x, t
        for i in (x-1, x+1, x*2):
            if 0 <= i < MAX:
                if visited[i] == -1:
                    visited[i] = x
                    q.append((i, t+1))
result = bfs(n)
print(result[1])
temp = k
temp_l = [k]
for _ in range(result[1]):
    temp_l.append(visited[temp])
    temp = visited[temp]
for i in temp_l[::-1]:
    print(i, end=' ')