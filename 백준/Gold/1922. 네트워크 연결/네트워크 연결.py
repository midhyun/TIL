import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    parentA = find(parent, a)
    parentB = find(parent, b)

    if parentA < parentB:
        parent[parentB] = parentA
    else:
        parent[parentA] = parentB

N, M = int(input()), int(input())
parent = [0]*(N+1)
edges = []

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)