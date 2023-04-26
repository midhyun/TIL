import sys
sys.stdin = open('1248_Guess.txt')
input = sys.stdin.readline

N = int(input())
sign = list(input().rstrip())
graph = [[0]*N for _ in range(N)]
idx = 0
for i in range(N):
    for j in range(i, N):
        if sign[idx] == '+':
            signal = 1
        elif sign[idx] == '-':
            signal = -1
        else:
            signal = 0
        graph[i][j] = signal
        idx += 1
nums = [0]*N

def check(idx):
    sum_tmp = 0
    for i in range(idx, -1, -1):
        sum_tmp += nums[i]
        if sum_tmp != 0 and graph[i][idx] == 0 : return False
        if sum_tmp <= 0 and graph[i][idx] == 1 : return False
        if sum_tmp >= 0 and graph[i][idx] == -1 : return False

    return True

def dfs(idx):
    if idx == N:
        print(*nums)
        exit()
    if graph[idx][idx] == 0:
        return dfs(idx+1)
    
    for i in range(1, 11):
        nums[idx] = graph[idx][idx] * i
        if check(idx):
            dfs(idx+1)

dfs(0)