import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('12978_스크루지민호2.txt')
input = sys.stdin.readline

YES = 1
NO = 0
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
# 2차원 해당 지점에 경찰서를 설치 했을 때, 안 했을 때.
dp = [[0]*(N+1) for _ in range(2)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(root):
    visited[root] = True
    # 설치 했으므로 경찰서 1개
    dp[YES][root] = 1
    # 인접노드, 자식으로, 사이클이 없는 트리구조이므로
    for child in graph[root]:
        if visited[child]: continue
        dfs(child)
        # bottom-up: 자식노드의 설치한 경우, 안한경우 중 더 유리한 경우를 더함.
        # 부모노드에 경찰서를 설치 안 한경우 자식은 설치되어있어야 함.
        # 즉, 없으면 설치해야되고, 있으면 설치와 미설치 중 이득인거 고르기로 단순화가 가능함.
        dp[YES][root] += min(dp[YES][child], dp[NO][child])
        dp[NO][root] += dp[YES][child]
dfs(1)  

print(min(dp[YES][1], dp[NO][1]))