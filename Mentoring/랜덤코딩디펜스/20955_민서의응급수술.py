import sys
sys.stidn = open('20955_민서의응급수술.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

# 사이클 있으면 연결 끊기
# 연결되어 있지 않은 트리는 잇기