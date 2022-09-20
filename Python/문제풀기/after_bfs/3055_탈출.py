import sys
sys.stdin = open('3055_탈출.txt')
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[i for i in input().strip()]for _ in range(n)]

goal = []
start = []
water = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'D':
            goal.append((i, j))
        elif graph[i][j] == '*':
            water.append((i, j))
        elif graph[i][j] == 'S':
            start.append((i, j))