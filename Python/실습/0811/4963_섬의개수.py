import sys
sys.setrecursionlimit(10**6)                # 런타임 오류 << 
sys.stdin = open('4963.txt')
input = sys.stdin.readline
def pprint(lst):
    for i in lst:
        print(i)
    print('---------------')
# 땅 1, 바다 0 # 섬의 개수 세기
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,1,0,-1,1,-1,1,0]                   

def check_island(i, j):                     # i, j 가 땅이면 0으로 바꾸고 방문처리,
    if island_map[i][j]:
        island_map[i][j] = 0
        island_bool[i][j] = True
        for k in range(8):                  # 델타 탐색으로 방문처리가 안된 곳에서 재귀 실행
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < w and 0 <= y < h:
                if not island_bool[y][x]:
                    check_island(y, x)
    else:
        return False

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0) :
        break
    island_map = [list(map(int, input().split())) for _ in range(h)]
    island_bool = [[False]*w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if island_map[i][j]:
                cnt += 1
                check_island(i, j)

    print(cnt)