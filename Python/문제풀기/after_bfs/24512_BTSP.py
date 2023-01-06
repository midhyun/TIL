import sys
sys.stdin = open('24512_BTSP.txt')
input = sys.stdin.readline

def tsp(idx, path):
    # 모든 정점을 방문했다면
    if path == (1<<n)-1:
        # 출발지로 가는 길이 있다면 출발지로 가는 비용 반환
        return graph[idx][0] if graph[idx][0] > 0 else INF
    # dp에 이미 값이 있다면
    if dp[idx][path] > 0:
        return dp[idx][path]

    temp = INF
    for i in range(1, n):
        # 정점 i 를 방문했거나, i로 가는 길이 없을 경우
        if (path>>i) % 2 == 1 or graph[idx][i] == 0: continue
        tmp = tsp(i, path|(1<<i))
        temp = min(temp, max(tmp, graph[idx][i]))
    dp[idx][path] = temp
    return temp

INF = int(1e9)
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
route = [0]*n
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = c
dp = [[0] * (1<<n) for _ in range(n)]

print(tsp(0, 1))
