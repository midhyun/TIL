import sys
sys.stdin = open('16918_봄버맨.txt')
input = sys.stdin.readline

R, C, N = map(int, input().split())
matrix = [[list(input().rstrip()) for _ in range(R)]]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
# 모든칸이 채워진 그래프(1)            
matrix.append([['O']*C for _ in range(R)])
# 처음 설치된 폭탄이 터진 그래프(2)
# t=0: 처음설치폭탄 터졌을때, t=2: 두번째설치폭탄터졌을때
def make_matrix(t):
    visited = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if matrix[t][i][j] == 'O':
                visited[i][j] = 1
                
    tmp = [['O']*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if visited[i][j]:
                tmp[i][j] = '.'
                for k in range(4):
                    y, x = i + dy[k], j + dx[k]
                    if 0 <= y < R and 0 <= x < C:
                        tmp[y][x] = '.'
    matrix.append(tmp)
for i in [0, 2]:
    make_matrix(i)

def result(cnt):
    res = matrix[cnt]        
    for mat in res:
        print(''.join(mat))
if N == 1:
    result(0)
elif N % 2 == 0:
    result(1)
elif N % 4 == 1:
    result(3)
elif N % 4 == 3:
    result(2)