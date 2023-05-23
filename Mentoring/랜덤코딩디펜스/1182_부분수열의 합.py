import sys
sys.stdin = open('1182_부분수열의 합.txt')
input = sys.stdin.readline

N, S = map(int, input().split())
int_list = [*map(int, input().split())]
check = [False]*N
cnt = 0
def dfs(num, check, cur):
    global cnt
    if num == S:
        cnt += 1
    
    for i in range(cur, N):
        if not check[i]:
            check[i] = True
            dfs(num + int_list[i], check, i)
            check[i] = False
for i in range(N):
    check[i] = True
    dfs(int_list[i], check, i)
    check[i] = False
print(cnt)