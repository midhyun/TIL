import sys
import copy
sys.stdin = open('1961_숫자배열회전.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    print(f'#{test_case}')
    n = int(input())
    graph = [input().strip().split() for _ in range(n)]
    result = []
    for i in range(n):
        result =['','','']
        for j in range(n):
            result[0] += graph[n-1-j][i]
            result[1] += graph[n-1-i][n-1-j]
            result[2] += graph[j][n-1-i]
        print(' '.join(i for i in result))