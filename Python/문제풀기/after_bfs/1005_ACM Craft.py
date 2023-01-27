import sys
from collections import deque
sys.stdin = open('1005_ACM Craft.txt')
input = sys.stdin.readline

def tpsort():
    result = [0] * (n+1)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result[now] += times[now]
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now])
            if indegree[i] == 0:
                q.append(i)
    return result[w]


t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    times =[0] + [*map(int, input().split())]
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())
    print(tpsort())