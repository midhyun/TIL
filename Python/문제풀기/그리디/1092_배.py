import sys
sys.stdin = open('1092_배.txt')
input = sys.stdin.readline

N = int(input())
limits = sorted([*map(int, input().split())], reverse=True)
M = int(input())
weights = sorted([*map(int, input().split())], reverse=True)
visited = [0]*(M)
cnt = 0; cur = 0
if limits[0] < weights[0]:
    print(-1)
else:
    positions = [0]*N
    while cnt < M:
        for i in range(N):
            while positions[i] < M:
                if not visited[positions[i]] and limits[i] >= weights[positions[i]]:
                    visited[positions[i]] = True
                    positions[i] += 1
                    cnt += 1
                    break
                positions[i] += 1
        cur += 1
    print(cur)