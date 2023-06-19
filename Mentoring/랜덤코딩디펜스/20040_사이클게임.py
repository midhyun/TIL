import sys
sys.stdin = open('20040_사이클게임.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    parent[a] = find(a)
    parent[b] = find(b)
    if parent[a] != parent[b]:
        

for _ in range(M):
    a, b = map(int, input().split())
