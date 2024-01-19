import sys
input = sys.stdin.readline

n = int(input())
INF = 100
graph = [[] for _ in range(26)]
distance = [[INF]*26 for _ in range(26)]
for _ in range(n):
    a, b = input().rstrip().split(' is ')
    a = ord(a) - 97
    b = ord(b) - 97
    graph[a].append(b)
    distance[a][b] = 1


for i in range(26):
    for j in range(26):
        if i == j:
            distance[i][j] = 0

for k in range(26):
    for i in range(26):
        for j in range(26):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

m = int(input())
for _ in range(m):
    a, b = input().rstrip().split(' is ')
    a = ord(a) - 97
    b = ord(b) - 97
    if distance[a][b] != INF:
        print('T')
    else:
        print('F')