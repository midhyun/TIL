import sys
sys.stdin = open('16991_외판원 순회3.txt')
input = sys.stdin.readline

def tsp(idx, path):
    if path == (1 << n) -1:
        return graph[idx][0] if graph[idx][0] > 0 else INF
    if dp[idx][path] > 0:
        return dp[idx][path]
    
    temp = INF
    for i in range(1, n):
        if (path>>i) % 2 == 1 or graph[idx][i] == 0: continue
        temp = min(temp, graph[idx][i] + tsp(i, path|(1<<i)))
    dp[idx][path] = temp
    return temp

INF = int(1e9)
n = int(input())
dp = [[0]*(1<<n) for _ in range(n)]
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))

graph = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        graph[i][j] = ((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2)**(0.5)

print(tsp(0, 1))