import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append([*map(int, input().split())])

status = input().strip()
P = int(input())

dp = [1000] * (1 << N)
q = deque()

time, now = 0, 0
for i in range(len(status)):
    if status[-i-1] == 'Y':
        time += 1
        now += 2 ** i

def solution(time, now):
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
        for _ in range(size):
            now, cost = q.popleft()
            for i in range(N):
                if (1 << i) & now == 0:
                    tmp = sys.maxsize
                    for j in range(N):
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