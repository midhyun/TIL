import sys
sys.stdin = open('1987_알파벳.txt')
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]

r ,c = map(int, input().split())
graph = [[i for i in input().strip()] for _ in range(r)]

def bfs():
    q = set([(0, 0, graph[0][0])])
    result = 1
    while q:
        i, j, d = q.pop()
        result = max(result, len(d))
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= x < r and 0 <= y < c and graph[y][x] not in d:
                q.add((y, x, graph[y][x] + d))
                print(q)
    return result

print(bfs())