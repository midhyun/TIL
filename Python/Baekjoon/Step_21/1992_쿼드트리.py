import sys
sys.stdin = open('1992_쿼드트리.txt')
input = sys.stdin.readline

n = int(input())
graph = [[int(i) for i in input().strip()] for _ in range(n)]
result = []
def zipp(y, x, n):
    color = graph[y][x]
    z = int(n/2)
    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j] != color:
                result.append('(')
                zipp(y, x, z)
                zipp(y, x+z, z)
                zipp(y+z, x, z)
                zipp(y+z, x+z, z)
                result.append(')')
                return
    if color == 1:
        result.append('1')
    else:
        result.append('0')
zipp(0, 0, n)
print(''.join(result))