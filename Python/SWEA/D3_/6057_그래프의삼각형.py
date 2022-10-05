import sys
from collections import deque
sys.stdin = open('6057_그래프의삼각형.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        i, j = map(int,input().split())
        graph[i].append(j)
        graph[j].append(i)
    result = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i in graph[j] and j in graph[k] and k in graph[i]:
                    result += 1
    print(f'#{test_case} {result}')