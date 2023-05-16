import sys
input = sys.stdin.readline

scroll = input().rstrip()
graph = [input().rstrip(), input().rstrip()]
N = len(graph[0])

matrix = [[[0]*(N+1) for _ in range(2)] for _ in range(len(scroll)+1)]

for i in range(len(scroll)):
    cur = scroll[i]
    for j in range(2):
        tmp = 0 if i > 0 else 1
        for k in range(1, N+1):
            tmp += matrix[i-1][j-1][k-1]
            if graph[j][k-1] == cur:
                matrix[i][j][k] = tmp

print(sum(matrix[-2][0])+sum(matrix[-2][1]))