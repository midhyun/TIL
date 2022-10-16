import sys
sys.stdin = open('2630_색종이만들기.txt')
input = sys.stdin.readline

n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]
white = []
blue = []

def is_paper(y, x, n):
    color = graph[y][x]
    z = int(n/2)
    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j] != color:
                is_paper(y, x, z)
                is_paper(y+z, x, z)
                is_paper(y, x+z, z)
                is_paper(y+z, x+z, z)
                return
    if color == 0:
        white.append(1)
    else:
        blue.append(1)
is_paper(0, 0, n)

print(sum(white))
print(sum(blue))
