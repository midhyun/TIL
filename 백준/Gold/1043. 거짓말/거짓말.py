import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        return find_parent(parent[x])

def union_parent(a, b):
    parentA = find_parent(a)
    parentB = find_parent(b)

    if a < b: parent[parentB] = parentA
    else: parent[parentA] = parentB

N, M = map(int, input().split())
truthPeople = [*map(int, input().split())]
if truthPeople[0] == 0:
    print(M)
    exit(0)
parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

for i in range(1, len(truthPeople)):
    union_parent(truthPeople[1], truthPeople[i])

party = []
for _ in range(M):
    party.append([*map(int, input().split())])

for par in party:
    for i in range(1, len(par)):
        union_parent(par[i], par[1])

tmp = find_parent(truthPeople[1])
result = 0
for par in party:
    for i in range(1, len(par)):
        if tmp == find_parent(par[i]):
            break
    else:
        result += 1

print(result)