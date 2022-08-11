import sys
from collections import deque
sys.stdin = open('1926.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = deque()

lst = []
for idx_i in range(n):
    for idx_j in range(m):
        if paper[idx_i][idx_j]:                                          # 현재 위치에 색칠이 되어 있다면, 그림을 찾음.
            queue.append((idx_i, idx_j))
            visited[idx_i][idx_j] = True
            cnt = 1                                                      # 그림을 찾았다면 카운트 초기화 1
            while queue:                                                 # 행렬에서 현재 위치와 인접한 색칠된 부분들을 모두 0으로 바꾸어줌
                i, j = queue.popleft()
                for k in range(4):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= x < m and 0 <= y < n:
                        if visited[y][x] == False and paper[y][x] == 1:
                            visited[y][x] = True
                            paper[y][x] = 0
                            cnt += 1                                     # 색칠된 부분을 0으로 바꾸면서 개수를 카운트
                            queue.append((y, x))
            lst.append(cnt)                                              # 카운트한 개수를 리스트에 담아줌,
if len(lst) == 0:                                                        # 리스트에 담긴 값이 없다면 그림이 없음, 그림의 크기는 0으로 출력
    print(0, 0,sep = '\n')
else:                                                                    # 리스트에 담긴 그림의 크기의 개수 == 그림의 개수,
    print(len(lst), max(lst),sep = '\n')