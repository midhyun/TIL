import sys
input = sys.stdin.readline

# N, M 크기의 그래프
# 8방향 탐색, 재방문True
# 이동하면서 각 칸의 알파벳을 더함.
def dfs(i, j, cur):
    if len(cur) > 5:
        return
    
    if god_string.get(cur) != None:
        god_string[cur] += 1
        return
    
    for k in range(8):
        y, x = (i + dy[k])%N, (j + dx[k])%M
        dfs(y, x, cur+graph[y][x])

dy, dx = [0, 0, -1, 1, -1, 1, -1, 1], [-1, 1, 0, 0, -1, 1, 1, -1]
N, M, K = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
god_string = {}
result = []
for _ in range(K):
    gs = input().rstrip()
    result.append(gs)
    god_string[gs] = god_string.get(gs, 0)
    


for i in range(N):
    for j in range(M):
        dfs(i, j, graph[i][j])

for res in result:
    print(god_string[res])