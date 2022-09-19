import sys
sys.stdin = open('D2_2001.txt')
input = sys.stdin.readline

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(n)]
    flies = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for dy in range(m):
                y = i + dy
                for dx in range(m):
                    x = j + dx
                    cnt += graph[y][x]
            flies.append(cnt)
    print(f'#{test_case} {max(flies)}')