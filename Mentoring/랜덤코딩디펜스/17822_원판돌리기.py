import sys
from collections import deque
sys.stdin = open('17822_원판돌리기.txt')
input = sys.stdin.readline

def solution():
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    N, M, T = map(int, input().split())
    disk = [deque([*map(int, input().split())]) for _ in range(N)]

    def bfs(n, ii, ij):
        checkstack = [(ii, ij)]
        stack = [(ii, ij)]
        visited[ii][ij] = True

        while stack:
            i, j = stack.pop()
            for k in range(4):
                y = i + dy[k]
                x = (j + dx[k])%M
                
                if 0 <= y < N and disk[y][x] == n and not visited[y][x]:
                    visited[y][x] = True
                    stack.append((y, x))
                    checkstack.append((y, x))

        if len(checkstack) > 1:
            for i, j in checkstack:
                disk[i][j] = 0
            return True
        else:
            visited[ii][ij] = False
        return False

    def spinDisk(x, d, k):
        for i in range(x-1, N, x):
            if d == 0:
                for j in range(k):
                    disk[i].appendleft(disk[i].pop())
            else:
                for j in range(k):
                    disk[i].append(disk[i].popleft())

    for t in range(T):
        # x 배수의 원판을 d 방향으로 k칸 회전, d=0: 시계방향, d=1: 반시계방향
        # 회전 할 때마다 방문기록을 초기화 해줘야함.
        visited = [[False]*M for _ in range(N)]
        x, d, k = map(int, input().split())
        spinDisk(x, d, k)

        flag = False
        total = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and disk[i][j]:
                    if bfs(disk[i][j], i, j):
                        flag = True

        if not flag:
            for i in range(N):
                for j in range(M):
                    if disk[i][j]:
                        total += disk[i][j]
                        cnt += 1

            if cnt:
                avg = total/cnt
                for i in range(N):
                    for j in range(M):
                        if disk[i][j]:
                            if disk[i][j] > avg:
                                disk[i][j] -= 1
                            elif disk[i][j] < avg:
                                disk[i][j] += 1
         
    res = 0

    for i in range(N):
        for j in range(M):
            if disk[i][j]:
                res += disk[i][j]
    return res

print(solution())