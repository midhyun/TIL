import sys
sys.stdin = open('11403_경로찾기.txt')
input = sys.stdin.readline

n = int(input())
result = [[0]*n for _ in range(n)]
graph = [[] for _ in range(n)]
visited = [[False]*n for _ in range(n)]

for i in range(n):
    in_node = [*map(int, input().split())]
    for j in range(n):
        if in_node[j] == 1:
            graph[i].append(j)
            graph[j].append(i)

def dfs():

for i in range(n):
    
stack = []
stack.append()