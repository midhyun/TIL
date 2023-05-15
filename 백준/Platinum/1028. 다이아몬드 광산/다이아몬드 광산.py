import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [[*map(int, list(input().strip()))] for _ in range(R)]
ld = [[0]*(C+2) for _ in range(R+2)]
rd = [[0]*(C+2) for _ in range(R+2)]
lu = [[0]*(C+2) for _ in range(R+2)]
ru = [[0]*(C+2) for _ in range(R+2)]

for i in range(R-1, -1, -1):
    for j in range(C):
        if graph[i][j] == 1:
            x, y = j+1, i+1
            ld[y][x] = ld[y+1][x-1]+1
            rd[y][x] = rd[y+1][x+1]+1

for i in range(R):
    for j in range(C):
        if graph[i][j] == 1:
            x, y = j+1, i+1
            lu[y][x] = lu[y-1][x-1]+1
            ru[y][x] = ru[y-1][x+1]+1

result = 0
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