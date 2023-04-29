import sys
sys.stdin = open('17144_미세먼지안녕.txt')
input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(R)]
air_cleaner = []
for i in range(R):
    if graph[i][0] == -1:
        air_cleaner.append(i)

def bfs(i, j, tmp):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for k in range(4):
        x, y = j + dx[k], i + dy[k]
        if 0 <= y < R and 0 <= x < C and graph[y][x] >= 0:
            tmp[y][x] += graph[i][j]//5
            tmp[i][j] -= graph[i][j]//5

def wind(x, n):
    DIR = [[(0, 1), (-1, 0), (0, -1), (1, 0)], [(0, 1), (1, 0), (0, -1), (-1, 0)]]
    DIR = DIR[n]
    dir = 0
    tmp = 0
    cur = [x, 0]
    while True:
        if not (0 <= cur[0]+DIR[dir][0] < R and 0 <= cur[1]+DIR[dir][1] < C):
            dir = (dir + 1) % 4
            
        cur[0] += DIR[dir][0]
        cur[1] += DIR[dir][1]
        y, x = cur

        if graph[y][x] == -1:
            break

        graph[y][x], tmp = tmp, graph[y][x]



def cycle():
    tmp = [[0]*C for _ in range(R)]
    # 확산
    for i in range(R):
        for j in range(C):
            if graph[i][j] >= 0:
                bfs(i, j, tmp)
    
    for i in range(R):
        for j in range(C):
            graph[i][j] += tmp[i][j]
    
    #공기청정기
    wind(air_cleaner[0], 0)
    wind(air_cleaner[1], 1)


    
for _ in range(T):
    cycle()
    
result = 2
for g in graph:
    result += sum(g)
print(result)