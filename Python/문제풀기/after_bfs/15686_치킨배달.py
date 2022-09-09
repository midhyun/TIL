import sys
sys.stdin = open('15686_치킨배달.txt')
input = sys.stdin.readline

n, m = map(int ,input().split())
graph = [[*map(int, input().split())] for _ in range(n)]
house = []
shop = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        elif graph[i][j] == 2:
            shop.append((i,j))

for a in 