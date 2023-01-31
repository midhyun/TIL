import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    home = [*map(int, input().split())]
    graph = [[*map(int, input().split())] for _ in range(N)]
    penta = [*map(int, input().split())]
    visited = [False]*N

    q = deque()
    q.append(home)
    flag = False
    while q:
        i, j = q.popleft()
        dist = abs(penta[0] - i) + abs(penta[1] - j)
        if dist <= 1000:
            flag = True
            break
        for x in range(N):
            dist = abs(graph[x][0] - i) + abs(graph[x][1] - j)
            if not visited[x] and dist <= 1000:
                visited[x] = True
                q.append((graph[x][0], graph[x][1]))
    print('happy') if flag else print('sad')