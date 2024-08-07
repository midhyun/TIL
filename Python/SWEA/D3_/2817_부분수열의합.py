import sys
sys.stdin = open('2817_부분수열의합.txt')
input = sys.stdin.readline

def dfs(idx,sum):
    global cnt                      # 4
    sum += lst[idx]                 # 1 2 3 4 
    if sum == k:                    # 3
        cnt+=1
    else:
        for i in range(idx,n):
            if not visited[i]:
                visited[i] = 1
                dfs(i,sum)
                visited[i] = 0

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())            # k 목적 값
    lst = [*map(int, input().split())]
    cnt = 0
    for i in range(n):
        visited = [0] * n
        visited[i] = 1
        dfs(i, 0)
    print(f'#{test_case}', cnt)