import sys
from collections import deque
sys.stdin = open('11559_뿌요뿌요.txt')
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(start): # 연쇄 1
    q = deque()
    q.append(start)
    color = graph[start[0]][start[1]]
    visited[start[0]][start[1]] = True
    cnt = 1
    dit = False
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < 12 and 0 <= y < 6 and not visited[y][x] and graph[y][x] == color:
                visited[y][x] = True
                q.append((y, x))
                cnt += 1
    if cnt >= 4:
        dit=True
        for i in range(6):
            for j in range(12):
                if graph[i][j] == color:
                    graph[i][j] = '.'      
    return dit

def down():                                             # 뿌요뿌요 아래로 내리기
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11, j, -1):
                if graph[i][j] != '.' and graph[i][k] == '.':
                    graph[i][j], graph[i][k] = graph[i][k], graph[i][j]
                    break


graph_row = [[i for i in input().strip()] for _ in range(12)]
graph = [[0]*12 for _ in range(6)]
result = 0
for i in range(12):                     # 그래프 전치
    for j in range(6):
        graph[j][i] = graph_row[i][j]


while True:
    visited = [[False]*12 for _ in range(6)]# 뿌요뿌요 1연쇄
    check = False
    for i in range(6):                      
        for j in range(12):
            if graph[i][j] != '.':
                if bfs((i, j)):
                    check = True
    if check:
        down()
    elif not check:
        break
    result += 1

print(result)