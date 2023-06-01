import sys
from collections import deque
sys.stdin = open('9079_동전게임.txt')
input = sys.stdin.readline



def bfs(start):
    visited = [-1]*(1<<9)
    case = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        cur = q.popleft()
        if cur == 0 or cur == 511:
            return visited[cur]
        for c in case:
            nxt = cur
            for i in c:
                nxt ^= 1<<i
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
    return -1

def solution(graph):
    cur, cnt = 0, 0
    for i in range(3):
        for j in range(3):
            tmp = 0 if graph[i][j] == 'H' else 1
            if tmp:
                cur += 1<<cnt
            cnt += 1
    return bfs(cur)
# 9칸을 2가지, 전체경우의 수...2^9 = 512가지

T = int(input())
for _ in range(T):
    graph = [input().split() for _ in range(3)]
    print(solution(graph))