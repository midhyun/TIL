import sys
from collections import deque
sys.stdin = open('14867_물통.txt')
input = sys.stdin.readline

target = [*map(int, input().split())]
matrix = [[0]*(target[1]+1) for _ in range(target[0]+1)]
def bfs(target):
    q = deque()
    q.append((0,0,0))
    matrix[0][0] == 1
    while q:
        a,b,c = q.popleft()
        if a == target[2] and b == target[3]:
            return c
        if not matrix[target[0]][b]:
            q.append((target[0],b,c+1))
            matrix[target[0]][b] = c+1
        if not matrix[a][target[1]]:
            q.append((a,target[1],c+1))
            matrix[a][target[1]] = c+1
        if not matrix[0][b]:
            q.append((0,b,c+1))
            matrix[0][b] = c+1
        if not matrix[a][0]:
            q.append((a,0,c+1))
            matrix[a][0] = c+1
        if target[1] <= a + b:
            temp = (a+b-target[1],target[1],c+1)
        else:
            temp = (0, a+b, c+1)
        if not matrix[temp[0]][temp[1]]:
            q.append(temp)
            matrix[temp[0]][temp[1]] = c+1
        if target[0] <= a + b:
            temp2 = (target[0], a+b-target[0],c+1)
        else:
            temp2 = (a+b, 0, c+1)
        if not matrix[temp2[0]][temp2[1]]:
            q.append(temp2)
            matrix[temp2[0]][temp2[1]] = c+1
    return -1

print(bfs(target))