import sys
from collections import deque
sys.stdin = open('1102_발전소.txt')
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append([*map(int, input().split())])

status = input().strip()
P = int(input())
# 모든 경우의 수 dp
dp = [1000] * (1 << N)


time, now = 0, 0
for i in range(len(status)):
    if status[-i-1] == 'Y':
        time += 1
        now += 2 ** i

def solution(time, now):
    q = deque()
    dp[now] = 0
    answer = 1000
    if P == 0 or time >= P:
        return 0
    elif time == 0:
        return -1
    else:
        q.append((now, 0))
        
    while time < P:
        size = len(q)
        print(q)
        for _ in range(size):
            now, cost = q.popleft()
            for i in range(N):
                # 현재 i 번째 발전소가 꺼져있는 경우
                if (1 << i) & now == 0:
                    tmp = sys.maxsize
                    for j in range(N):
                        # 켜져있는 j번째 발전기로 i번째 발전기를 켜는 비용
                        if (1 << j) & now == 1 << j:
                            tmp = min(tmp, graph[N-1-j][N-1-i])
                    if dp[now + (1 << i)] > cost + tmp:
                        q.append((now + (1 << i), cost + tmp))
                        dp[now + (1 << i)] = cost + tmp
        time += 1
    
    while q:
        _, cost = q.pop()
        answer = min(answer, cost)
    return answer

print(solution(time, now))