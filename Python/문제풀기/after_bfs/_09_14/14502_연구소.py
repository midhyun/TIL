import sys
from collections import deque
from itertools import combinations
import copy
sys.stdin = open('14502_연구소.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
graph =[[*map(int, input().split())] for _ in range(n)]
blanks = []
virus = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blanks.append((i,j))
        if graph[i][j] == 2:
            virus.append((i,j))

def bfs(start, combie):
    result = 0    
    q = deque()
    graph_c = copy.deepcopy(graph)
    for wall in combie:
        graph_c[wall[0]][wall[1]] = 1
    for z in start:
        q.append(z)
        while q:
            i, j = q.popleft()
            for k in range(4):
                x = j + dx[k]
                y = i + dy[k]
                if 0 <= x < m and 0 <= y < n:
                    if graph_c[y][x] == 0:
                        graph_c[y][x] = 2
                        q.append((y,x))
        
    for i in graph_c:
        for j in i:
            if j == 0:
                result += 1            
    return result

max_result = 0    
for combie in combinations(blanks, 3):
    max_result = max(bfs(virus, combie), max_result)
    
        
print(max_result)