import sys
sys.stdin = open('1028_다이아몬드광산.txt')
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [[*map(int, list(input().strip()))] for _ in range(R)]
# dp 4방향 메모이제이션 인덱스범위를 위해 R, C 각각 +2
ld = [[0]*(C+2) for _ in range(R+2)]
rd = [[0]*(C+2) for _ in range(R+2)]
lu = [[0]*(C+2) for _ in range(R+2)]
ru = [[0]*(C+2) for _ in range(R+2)]

# 맨 아래칸 부터 최상단까지,
# graph[i][j] 가 1이면, 좌하단, 우하단의 dp값 +1
for i in range(R-1, -1, -1):
    for j in range(C):
        if graph[i][j] == 1:
            x, y = j+1, i+1
            ld[y][x] = ld[y+1][x-1]+1
            rd[y][x] = rd[y+1][x+1]+1
# 맨 윗칸 부터 최하단까지,
# graph[i][j] 가 1이면, 좌상단, 우상단의 dp값 +1
for i in range(R):
    for j in range(C):
        if graph[i][j] == 1:
            x, y = j+1, i+1
            lu[y][x] = lu[y-1][x-1]+1
            ru[y][x] = ru[y-1][x+1]+1

result = 0
# 그래프 전체를 순회하면서 현재위치가 다이아몬드의 상단 꼭지점일 경우 가능한 가장 큰 다이아몬드의 크기 = tmp
# 좌하단, 우하단의 min값, 1부터 min값 크기의 다이아몬드를 확인
# 2*(k-1) 만큼 아래로 떨어진 점 = 다이아몬드의 하단 꼭지점
# 하단 꼭지점으로부터 좌상단 우상단의 길이가 k이상이면 k크기의 다이아몬드
for i in range(R):
    for j in range(C):
        tmp = 0
        x, y = j+1, i+1
        for k in range(1, min(ld[y][x], rd[y][x])+1):
            if i+2*(k-1) < R:
                if graph[i+2*(k-1)][j] and lu[y+2*(k-1)][x] >= k and ru[y+2*(k-1)][x] >= k:
                    tmp = max(tmp, k)
        result = max(result, tmp)

print(result)