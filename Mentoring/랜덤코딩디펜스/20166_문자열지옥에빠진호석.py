import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('20166_문자열지옥에빠진호석.txt')
input = sys.stdin.readline

def dfs(i, j, cur):
    if len(cur) > mx:
        return
    
    if god_string.get(cur):
        god_string[cur] += 1
    
    for k in range(8):
        y, x = (i + dy[k]) % N, (j + dx[k]) % M
        dfs(y, x, cur+graph[y][x])

dy, dx = [0, 0, -1, 1, -1, 1, -1, 1], [-1, 1, 0, 0, -1, 1, 1, -1]
N, M, K = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
god_string, result, mx = {}, [], 0

for _ in range(K):
    gs = input().rstrip()
    mx = max(mx, len(gs))
    result.append(gs)
    god_string[gs] = 1

for i in range(N):
    for j in range(M):
        dfs(i, j, graph[i][j])

for res in result:
    print(god_string[res]-1)