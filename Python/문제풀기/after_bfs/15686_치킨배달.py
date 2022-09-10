import sys
from itertools import combinations
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

c_dist_min = 1e9
for combi in combinations(shop, m):
    c_dist = 0
    for home in house:
        c_dist += min([abs(home[0]-i[0]) +  abs(home[1]-i[1]) for i in combi])
        if c_dist_min <= c_dist: break
    if c_dist < c_dist_min: c_dist_min = c_dist

print(c_dist_min)