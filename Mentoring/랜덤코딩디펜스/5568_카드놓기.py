import sys
sys.stdin = open('5568_카드놓기.txt')
input = sys.stdin.readline

def dfs(depth, cur):
    if depth == K:
        result.add(cur)
    
    for i in range(N):
        if not check[i]:
            check[i] = True
            dfs(depth+1, cur+nums[i])
            check[i] = False
            
N = int(input())
K = int(input())
nums = []
for _ in range(N):
    nums.append(input().rstrip())
result = set()
check = [False]*(N)


for i in range(N):
    check[i] = True
    dfs(1, nums[i])
    check[i] = False

print(len(result))