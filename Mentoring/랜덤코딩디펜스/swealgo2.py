import sys
sys.stdin = open('swealgo2.txt')
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T+1):
    N, M, Q = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(N)]
    safe = set()
    check_i = [0]*N
    check_j = [0]*M
    for i in range(N):
        for j in range(M):
            check_i[i] = max(check_i[i], graph[i][j])
            check_j[j] = max(check_j[j], graph[i][j])
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == check_i[i] and graph[i][j] == check_j[j]:
                safe.add(graph[i][j])
    res = 0
    for _ in range(Q):
        r, c, x = map(int, input().split())
        r -= 1
        c -= 1

        graph[r][c] = x
        if check_i[r] < x:
            safe.discard(check_i[r])
            check_i[r] = x
        if check_j[c] < x:
            safe.discard(check_j[c])
            check_j[c] = x
        
        if check_i[r] == x and check_j[c] == x:
            safe.add(x)
        
        res += len(safe)
    print(f'#{test_case} {res}')

