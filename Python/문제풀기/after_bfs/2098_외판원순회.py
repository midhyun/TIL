import sys
sys.stdin = open('2098_외판원순회.txt')
input = sys.stdin.readline

def tsp(idx, path):
    # 모든 도시들을 방문했다고 현위치에서 시작지점까지 길이 있다면, 비용 리턴
    if path == total:
        return table[idx][0] if table[idx][0] > 0 else INF
    # 이미 최소경로를 계산했다면,
    if dp[idx][path] > 0:
        return dp[idx][path]
        
    temp = INF
    for i in range(1, n):
        # i번째 도시 방문확인 idx > i 도시까지의 길이 없다면 continue
        if (path >> i)%2 == 1 or table[idx][i] == 0: continue
        # i번째 도시를 방문한적없고, 길이 있다면
        temp = min(temp, table[idx][i] + tsp(i, path|(1<<i)))
        # path|(1<<i) == 지금까지 경로에 i번째 도시 방문처리
    # dp[현재위치][경로] = 최단거리
    dp[idx][path] = temp
    return temp

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(1<<n) for _ in range(n)]
total = (1<<n)-1
INF = int(1e9)
print(tsp(0, 1)) # 0번도시에서 출발