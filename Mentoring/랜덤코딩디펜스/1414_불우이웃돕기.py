import sys
sys.stdin = open('1414_불우이웃돕기.txt')
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
parent = [0] * N
result = 0
for i in range(N):
    parent[i] = i
edges = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != '0':
            len_LAN = ord(graph[i][j])
            graph[i][j] = len_LAN - 96 if len_LAN > 90 else len_LAN - 38
        else:
            graph[i][j] = 0
        if graph[i][j]:
            edges.append((graph[i][j], i, j))
        result += graph[i][j]

edges.sort()

def kruskal(result):
    cnt = 0
    for edge in edges:
        if cnt >= N-1:
            break
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result -= cost
            cnt += 1

    if cnt == N-1:
        return result
    else:
        return -1

print(kruskal(result))