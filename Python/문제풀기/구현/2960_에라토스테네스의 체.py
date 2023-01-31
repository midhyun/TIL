import sys
sys.stdin = open('2960_에라토스테네스의 체.txt')
input = sys.stdin.readline
# 2부터 nums리스트 에서 방문시 True인 값은 소수이다.
# 소수로 나누어지는 숫자는 소수가 아니다. >> False
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