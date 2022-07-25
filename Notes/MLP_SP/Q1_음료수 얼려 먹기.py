import sys
sys.stdin = open('input.txt')
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y]  == 0: # 현재위치에서 아직 방문안했다면
        graph[x][y] = 1 # 방문처리 !
        dfs(x - 1, y) # 함수안에서 함수를 재귀적 호출!
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)