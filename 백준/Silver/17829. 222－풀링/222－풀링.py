import sys
input = sys.stdin.readline

N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]

def solution(N, i, j):
    n = N//2
    if N == 1:
        return graph[i][j]
    tmp = [
        solution(n, i, j),
        solution(n, i+n, j),
        solution(n, i, j+n),
        solution(n, i+n, j+n),
    ]
    tmp.sort()
    return tmp[-2]

print(solution(N, 0, 0))