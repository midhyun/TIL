import sys
input = sys.stdin.readline

def dfs(depth, cur):
    if depth == K:
        result.add(cur)
        return
    
    for i in range(N):
        if not check[i]:
            check[i] = True
            dfs(depth+1, cur + nums[i])
            check[i] = False

N = int(input())
K = int(input())
nums = []
for _ in range(N):
    nums.append(input().rstrip())
result = set()
check = [False]*N

dfs(0, '')
print(len(result))