import sys
sys.stdin = open('5568_카드놓기.txt')
input = sys.stdin.readline

def dfs(depth, cur):
    # 종료조건을 넣고 리턴을 안넣어서 실제로 재귀가 종료되지 않았다.
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