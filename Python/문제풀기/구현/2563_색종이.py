import sys
sys.stdin = open('2563_색종이.txt')
input = sys.stdin.readline

N = int(input())
graph = [[0]*101 for _ in range(101)]
# 100x100 0인 그래프에 색종이를 놓은부분을 1로 치환
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            graph[a+i][b+j] = 1
# 1의 개수를 모두 더함
result = 0
for grap in graph:
    result += sum(grap)

print(result)