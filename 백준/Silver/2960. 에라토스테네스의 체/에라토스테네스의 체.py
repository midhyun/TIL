import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [1] * (N+1)
cnt = 0
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if nums[j] == 1:
            cnt += 1
            nums[j] = 0
        if cnt == K:
            print(j)
            exit()
print(cnt)