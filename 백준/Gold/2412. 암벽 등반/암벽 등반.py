import sys
from collections import deque
input = sys.stdin.readline

N, T = map(int, input().split())
matrix = set()
for _ in range(N):
    x, y = map(int, input().split())
    matrix.add((y, x))

def bfs():
    q = deque()
    q.append((0, 0, 0))

    while q:
        i, j, cnt = q.popleft()
        for dy in range(-2, 3):
            y = i + dy
            if 0 <= y < T+1:
                for dx in range(-2, 3):
                    x = j + dx
                    if (y, x) in matrix:
                        q.append((y, x, cnt+1))
                        matrix.remove((y, x))
                        if y == T:
                            return cnt+1

    
    return -1

print(bfs())