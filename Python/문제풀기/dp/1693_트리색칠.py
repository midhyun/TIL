import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('1693_트리색칠.txt')
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
# 최대 색은 16개이다 log2*n 개
# dp[i][color] : i번째 노드를 color로 색칠했을 때 최소 값
dp = [[0] * 17 for _ in range(n + 1)]
visited = [False] * (n + 1)

# DFS로 트리를 순회함.
def dfs(idx):
    # idx와 인접한 노드
    for i in graph[idx]:
        if visited[i]:
            continue
        visited[i] = True
        # DFS 재귀
        dfs(i)

        for j in range(1, 17): # 이전 색
            m_num = 100000000
            for k in range(1, 17): # 현재 색
                # 이전에 칠한 색과 현재 색이 다를 경우, 최솟값으로 갱신
                if j != k:
                    if m_num > dp[i][k]:
                        m_num = dp[i][k]
            # 최솟값을 더해준다.
            dp[idx][j] += m_num

    for i in range(1, 17):
        dp[idx][i] += i

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1] = True
dfs(1)
print(min(dp[1][1:]))