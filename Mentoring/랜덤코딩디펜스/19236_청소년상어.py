import sys
import copy
sys.stdin = open('19236_청소년상어.txt')
input = sys.stdin.readline

dy, dx = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
graph1 = []
for _ in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    graph1.append([[a1, b1-1], [a2, b2-1], [a3, b3-1], [a4, b4-1]])

pos = (0, 0, graph1[0][0][1])
result = graph1[0][0][0]
graph1[0][0] = 0

def dfs(graph, pos):
    res = 0
    # 물고기 이동
    for num in range(1, 17):
        flag = False
        for i in range(4):
            if flag: break
            for j in range(4):
                if flag: break
                if graph[i][j] and graph[i][j][0] == num:
                    dir = graph[i][j][1]
                    for _ in range(8):
                        y = i + dy[dir]
                        x = j + dx[dir]
                        if 0 <= y < 4 and 0 <= x < 4 and graph[y][x]:
                            graph[i][j][1] = dir
                            graph[y][x], graph[i][j] = graph[i][j], graph[y][x]
                            flag = True
                            break
                        dir += 1
                        dir %= 8
                    else:
                        flag = True
                        break
    for g in graph:
        print(g)
    print('-------------------', pos)
    # 상어 이동
    for k in range(1, 4):
        i, j, dir = pos
        y = i + (dy[dir]*k)
        x = j + (dx[dir]*k)
        if 0 <= y < 4 and 0 <= x < 4 and graph[y][x]:
            ngraph = copy.deepcopy(graph)
            npos = (y, x, graph[y][x][1])
            ngraph[y][x] = 0
            res = max(res, dfs(ngraph, npos) + graph[y][x][0])

    return res

print(dfs(graph1, pos)+result)
print(result)