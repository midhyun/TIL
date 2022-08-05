import sys
sys.stdin = open('9455.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    n, m = map(int, input().split())
    tetris = [list(map(int, input().split())) for _ in range(n)]    # 기존 행렬
    tetris_row = [[0]*n for _ in range(m)]                          # 전치 행렬

    for i in range(m):                                              # 행렬 전치
        for j in range(n):
            tetris_row[i][j] = tetris[j][i]
    cnt = 0
    for i in range(n):                                              # 검은칸이면 전치행렬에서 현재칸 이후의 빈칸의 갯수를 세어줌
        for j in range(m):
            if tetris[i][j] == 1:
                cnt += tetris_row[j][i:].count(0)
    print(cnt)