import sys
sys.stdin = open('15664_N과M10.txt')
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    seq = [*map(int, input().split())]
    seq.sort()
    visited = [False]*N
    result = []

    def dfs(n):
        
        if len(result) == M:
            print(*result)
            return
        
        check = 0
        for i in range(n, N):
            if not visited[i] and check != seq[i]:
                result.append(seq[i])
                visited[i] = True
                check = seq[i]
                dfs(i+1)
                result.pop()
                visited[i] = False
    
    dfs(0)

solution()