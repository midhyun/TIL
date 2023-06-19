import sys
sys.stdin = open('20040_사이클게임.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0]*(N)
for i in range(N):
    parent[i] = i

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else: parent[parent_a] = parent_b
        

for i in range(M):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i+1)
        break
else:
    print(0)
