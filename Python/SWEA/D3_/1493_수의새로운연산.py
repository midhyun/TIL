import sys
sys.stdin = open('1493_수의새로운연산.txt')
input = sys.stdin.readline

t = int(input())
cnt = 1
graph = [[0]*302 for _ in range(302)]
for i in range(2, 303):
    for j in range(1, i):
        graph[i-j][j] = cnt
        cnt += 1
for i in range(2, 302):
    for j in range(i, 302):
        graph[301+i-j][j] = cnt
        cnt += 1
for test_case in range(1, t+1):
    n, m = map(int ,input().split())
    for i in range(302):
        for j in range(302):
            if graph[i][j] == n:
                nn = (i, j)
            if graph[i][j] == m:
                nm = (i, j)
    y, x = nn[0]+nm[0], nn[1]+nm[1]
    print(graph[y][x])