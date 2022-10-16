import sys
sys.stdin = open('1780_종이의개수.txt')
input = sys.stdin.readline

n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]
result = []

def is_paper(y, x, n):
    color = graph[y][x]
    z = int(n/3)
    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j] != color:
                is_paper(y, x, z)
                is_paper(y, x+z, z)
                is_paper(y, x+(2*z), z)
                is_paper(y+z, x, z)
                is_paper(y+z, x+z, z)
                is_paper(y+z, x+(2*z), z)
                is_paper(y+(2*z), x, z)
                is_paper(y+(2*z), x+z, z)
                is_paper(y+(2*z), x+(2*z), z)
                return
    if color == -1:
        result.append(-1)
    elif color == 0:
        result.append(0)
    elif color == 1:
        result.append(1)
is_paper(0, 0, n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))