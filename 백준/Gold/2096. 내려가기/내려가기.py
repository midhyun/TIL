import sys
input = sys.stdin.readline

n = int(input())
dp = []
max_val = [0]*3
min_val = [0]*3

for i in range(n):
    a, b, c = map(int, input().split())
    graph = [a, b, c]

    temp_0 = max(max_val[0]+graph[0], max_val[1]+graph[0])
    temp_1 = max(max_val[0]+graph[1], max_val[1]+graph[1], max_val[2]+graph[1])
    temp_3 = max(max_val[1]+graph[2], max_val[2]+graph[2])
    min_temp_0 = min(min_val[0]+graph[0], min_val[1]+graph[0])
    min_temp_1 = min(min_val[0]+graph[1], min_val[1]+graph[1], min_val[2]+graph[1])
    min_temp_2 = min(min_val[1]+graph[2], min_val[2]+graph[2])

    max_val = [temp_0, temp_1, temp_3]
    min_val = [min_temp_0, min_temp_1, min_temp_2]
    dp = (max_val, min_val)

print(max(dp[0]), min(dp[1]))