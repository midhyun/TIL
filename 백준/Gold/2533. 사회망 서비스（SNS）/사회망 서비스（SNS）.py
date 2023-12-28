import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 부모노드가 일반인일 경우, 자식 노드는 전부 얼리어답터가 되어야 함.
# 부모노드가 얼리어답터일 경우, 자식 노드는 얼리어답터일 경우와 아닐 경우 중 더 작은값을 선택.
def find(x):
    visited[x] = True
    # 0: 일반인 1: 얼리어답터
    dp[x][0], dp[x][1] = 0, 1

    for child in graph[x]:
        if not visited[child]:
            find(child)
            dp[x][0] += dp[child][1] # 내가 얼리어답터가 아닐 때
            dp[x][1] += min(dp[child][0], dp[child][1]) # 내가 얼리어답터일 때

N = int(input())
graph = [[] for _ in range(N+1)]
dp = [[0]*2 for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


find(1)
print(min(dp[1][0], dp[1][1]))