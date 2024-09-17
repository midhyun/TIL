import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def topological_sort(leaf_list, indegree, graph, info_children, visited):
    q = deque(leaf_list)
    root = []
    while q:
        cur = q.popleft()
        if not graph[cur]:
            root.append(cur)
            continue
        parents = []
        for nxt in graph[cur]:
            parents.append((indegree[nxt], nxt))
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
        info_children[min(parents)[1]].append(cur)
    return root

def solution():
    return

N = int(input())
people = input().rstrip().split()
M = int(input())
indegree = defaultdict(int)
info_children = defaultdict(list)
graph = defaultdict(list)
visited = defaultdict(bool)

for _ in range(M):
    a, b = input().rstrip().split()
    graph[a].append(b)
    indegree[b] += 1
    indegree[a] += 0

leaf_list = []
for name, indeg in indegree.items():
    if indeg == 0:
        leaf_list.append(name)

result = sorted(topological_sort(leaf_list, indegree, graph, info_children, visited))
print(len(result))
print(*result)
people.sort()
for person in people:
    print(person, end=" ")
    print(len(info_children[person]), end = "")
    print('', *sorted(info_children[person]))

solution()