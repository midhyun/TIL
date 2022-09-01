import sys
sys.stdin = open('11660_구간합구하기5.txt')
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
sgraph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        sgraph[i][j] = graph[i-1][j-1] + sgraph[i][j-1]
for i in range(1, n+1):
    for j in range(1, n+1):
        sgraph[i][j] += sgraph[i-1][j]
for i in range(m):
    y1,x1,y2,x2 = map(int, input().split())
    result = sgraph[y2][x2] - sgraph[y1-1][x2] - sgraph[y2][x1-1] + sgraph[y1-1][x1-1]
    print(result)