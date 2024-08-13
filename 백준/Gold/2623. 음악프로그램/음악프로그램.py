import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution(indegree, singer):
    q, result = deque(), []
    for key, value in indegree.items():
        if value == 0:
            q.append(key)

    while q:
        cur = q.popleft()
        for nxt in singer[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    
        result.append(cur)
    if len(result) != N: return [0]

    return result

N, M = map(int, input().split())
singer = [[] for _ in range(N+1)]
indegree = defaultdict(int)
for _ in range(M):
    order = [*map(int, input().split())]
    for idx in range(1, len(order)-1):
        singer[order[idx]].append(order[idx+1])
        indegree[order[idx+1]] += 1

for i in range(1, N+1):
    indegree[i]

for num in solution(indegree, singer):
    print(num)