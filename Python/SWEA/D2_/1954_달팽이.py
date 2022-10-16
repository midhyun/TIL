import sys
sys.stdin = open('1954_달팽이.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    print(f'#{test_case}')
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    now = [0,0]
    graph[0][0] = 1
    k = 0
    for i in range(2, n**2+1): # n * n +1
        now[0], now[1] = now[0]+dir[k][0], now[1]+dir[k][1]
        if 0 <= now[0] < n and 0 <= now[1] < n and graph[now[0]][now[1]] == 0:
            graph[now[0]][now[1]] = i
        else:
            now[0], now[1] = now[0]-dir[k][0], now[1]-dir[k][1]
            k += 1
            k %= 4
            now[0], now[1] = now[0]+dir[k][0], now[1]+dir[k][1]
            graph[now[0]][now[1]] = i
    for i in graph:
        print(*i)