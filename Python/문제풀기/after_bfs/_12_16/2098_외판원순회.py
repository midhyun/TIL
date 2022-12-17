import sys
import math
sys.stdin = open('2098_외판원순회.txt')
input = sys.stdin.readline

n = int(input())
INF = 999999
graph = [[*map(int, input().split())] for _ in range(n)] # graph[i][j] == i 에서 j 까지의 거리
dp = [[INF] * (1 << n) for _ in range(n)]
# dp[i][j] : i = 내 위치, j = 아직 방문하지 않은, 방문해야 할 노드 정보
# 들어가는 값은 남은 점들을 최적 경로로 돌았을 때의 총 거리

def dfs(start, visited) :
    # start : 현재 내 위치
    # visited : 방문 여부 정보를 담고 있음. 해당 비트가 0이면 방문하지 않은 것, 1이면 방문한 것
    if visited == (1 << n) - 1 : # 모든 정점 방문
        dp[start][visited] = graph[start][0]
        return graph[start][0]
    
    if dp[start][visited] != INF :
        return dp[start][visited]
    
    print(start, visited)
    for i in range(1, n) :
        if visited & (1 << i) : # 0번 점은 시작점이니까 패스하고 1부터 본다. 방문한 점이라면 pass
            continue
        # 그 다음 점까지의 거리 + 그 다음 점에 방문하고 나서 남은 점들을 최적 경로로 돌았을 때의 거리
        # 의 합이 가장 작은 점이 현재 visited 상태 최적 경로 상의 다음 점이 될 것이다.
        dp[start][visited] = min(dp[start][visited], dfs(i, visited | (1 << i)) + graph[start][i]) 
    
    return dp[start][visited]

print(dfs(0, 1))

# i == 위치, j == 아직 방문하지않은, 방문해야 할 노드 정보
# 들어가는 값은 남은 점들을 최정 경로로 돌았을 때의 총 거리
for d in dp:
    print(d)


