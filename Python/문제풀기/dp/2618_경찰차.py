import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('2618_경찰차.txt')
input = sys.stdin.readline

def cost(a, b):
    return abs(a[0] - b[0]) + abs(a[1]- b[1])

def solution(a, b):
    cur = max(a, b) + 1
    if cur > W+1:
        return 0

    if dp[a][b] != -1:
        return dp[a][b]

    x = solution(cur, b) + cost(events[a], events[cur])
    y = solution(a, cur) + cost(events[b], events[cur])

    dp[a][b] = min(x,y)
    return dp[a][b]

def route(a, b):
    if max(a, b) > W:
        return
    cur = max(a, b) + 1
    x = cost(events[cur], events[a])
    y = cost(events[cur], events[b])
    if dp[cur][b] + x < dp[a][cur] + y:
        print(1)
        route(cur, b)
    else:
        print(2)
        route(a, cur)
    return

N = int(input())
W = int(input())
events = [(1,1),(N,N)]
dp = [[-1]*(W+2) for _ in range(W+2)]

for _ in range(W):
    events.append(tuple(map(int, input().split())))

# dp[i][j] = 경찰차1 i번째 사건, 경찰차2 j번째 사건을 해결한 상황일때 최소비용
# 앞으로의 이동거리 중 최솟값

print(solution(0,1)) # 2, 3, 4, 5 
route(0, 1)