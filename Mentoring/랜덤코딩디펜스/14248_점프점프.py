import sys
from collections import deque
sys.stdin = open('14248_점프점프.txt')
input = sys.stdin.readline

N = int(input())
nums =[0] + [*map(int, input().split())]
S = int(input())

visited = [False]*(N+1)

def bfs(S, visited, nums):
    q = deque()
    q.append(S)
    visited[S] = True
    while q:
        x = q.popleft()
        nxt1 = x + nums[x]
        nxt2 = x - nums[x]
        if 0 < nxt1 <= N:
            visited[nxt1] = True
            q.append(nxt1)
        if 0 < nxt2 <= N:
            visited[nxt2] = True
            q.append(nxt2)
    
    return sum(visited)

print(bfs(S, visited, nums))
