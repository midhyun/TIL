import sys
from collections import deque
sys.stdin = open('7562_나이트의 이동.txt')
input = sys.stdin.readline
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]
t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    (i_s, j_s) = map(int,input().split())
    (i_g, j_g) = map(int, input().split())
    q = deque()
    q.append((i_s, j_s, 0))
    cnt = 0
    result = 0
    while q:
        i, j, depth = q.popleft()
        if i == i_g and j == j_g:
            result = depth
            break
        cnt += 1
        for k in range(8):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < n and 0 <= y < n and not visited[y][x]:
                visited[y][x] = True
                q.append((y, x, depth +1))
    print(depth)