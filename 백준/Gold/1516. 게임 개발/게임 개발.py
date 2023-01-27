import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
indegree = [0] *(n+1)
times = [0] *(n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    temp = [*map(int, input().split())]
    times[i] = temp[0]
    for j in range(1, len(temp)-1):
        indegree[i] += 1
        graph[temp[j]].append(i)

def topology_sort():
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
    return result

tpsort = topology_sort()
for i in range(1, n+1):
    print(tpsort[i])
