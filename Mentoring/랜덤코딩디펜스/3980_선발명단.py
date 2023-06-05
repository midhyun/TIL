import sys
sys.stdin = open('3980_선발명단.txt')
input = sys.stdin.readline

def dfs(visited, pos, value):
    global result

    if pos == 11:
        result = max(result, value)
        return

    for i in range(11):
        if not visited[i] and graph[i][pos]:
            visited[i] = True
            dfs(visited, pos+1, value + graph[i][pos])
            visited[i] = False
    return

C = int(input())
for _ in range(C):
    graph = [[*map(int, input().split())] for _ in range(11)]
    visited = [False] * 11
    result = 0
    dfs(visited, 0, 0)
    print(result)