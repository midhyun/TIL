import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('2026_소풍.txt')
input = sys.stdin.readline

def dfs(friends, cur):
    if len(friends) == K:
        for friend in friends:
            print(friend)
        exit()

    for nxt in range(cur+1, N+1):
        if not visited[nxt]:
            for friend in friends:
                if friend not in graph[nxt]:
                    break
            else:
                visited[nxt] = True
                dfs(friends+[nxt], nxt)

K, N, F = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(F):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, N+1):
    visited = [False]*(N+1)
    visited[i] = True
    dfs([i], i)

print(-1)