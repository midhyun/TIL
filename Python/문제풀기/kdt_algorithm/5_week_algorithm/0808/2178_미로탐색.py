import sys
sys.stdin = open('2178.txt')
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
# def pprint(lst):
#     for i in lst:
#         print(i)
#     print('-----------------')
maze_ = [[int(i) for i in input().strip()] for _ in range(n)]       # 미로 행렬 
check_maze = [[False]*m for _ in range(n)]                          # 불리언 행렬 [False] n x m

dx = [1, -1, 0, 0]                                                  # 델타 
dy = [0, 0, 1, -1]
lst = deque()                                                       # 다음 확인할 요소 큐
def maze_runner(i, j):
    check_maze[i][j] = True                                         # 확인한 요소를 True
    lst.append((i, j))                                              # 큐에 값을 추가함
    while lst:
        i, j = lst.popleft()                                        # 큐에서 값을 꺼냄
        for idx in range(4):
            y = i + dy[idx]
            x = j + dx[idx]
            if 0 <= x < m and 0 <= y < n:                           # 미로 범위 안에서
                if maze_[y][x] == 1 and check_maze[y][x] == False:  # 델타 탐색 범위에서 1이고, 아직 확인하지 않은 요소는
                    maze_[y][x] = maze_[i][j] + 1                   # 1을 더해주고 
                    lst.append((y, x))                              # 큐에 다음 탐색 위치를 넣어줌
        # pprint(maze_)
maze_runner(0, 0)
print(maze_[n-1][m-1])