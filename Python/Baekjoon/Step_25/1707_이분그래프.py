import sys
from collections import deque
sys.stdin = open('1707_이분그래프.txt')
input = sys.stdin.readline

k = int(input())
def bfs(num):
    q = deque()
    q.append(num)
    visited[num] = 1
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = -visited[cur]
                q.append(i)
            elif visited[i] == visited[cur]:
                return False
    return True
            


for test_case in range(1,k+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    flag = 1
    for i in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, v+1):
        if visited[i] == 0:
            if not bfs(i):
                flag = 0
                break
    print('YES' if flag else 'NO')