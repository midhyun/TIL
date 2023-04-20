import sys
from collections import deque
sys.stdin = open('1941_소문난칠공주.txt')
input = sys.stdin.readline

matrix = []
for _ in range(5):
    matrix.append(list(input().rstrip()))
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(arr):
    visited = [[False]*5 for _ in range(5)]
    check = 1
    for i, j in arr:
        visited[i][j] = True
    q = deque()
    q.append(arr[0])
    visited[arr[0][0]][arr[0][1]] = False

    while q:
        i, j = q.popleft()

        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < 5 and 0 <= x < 5 and visited[y][x]:
                visited[y][x] = False
                q.append((y, x))
                check += 1

    if check == 7:
        return True
    else:
        return False


def dfs(depth, cur, cnt):
    global result

    if cnt >= 4:
        return
    
    if depth == 7:
        if bfs(arr):
            result += 1
        return
    
    for i in range(cur, 25):
        y = i // 5 # i의 몫은 행
        x = i % 5 # i의 나머지는 열
        arr.append((y, x))
        dfs(depth+1, i+1, cnt + (matrix[y][x] == 'Y'))
        arr.pop()

result = 0
arr = []
dfs(0, 0, 0)
print(result)
