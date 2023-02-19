import sys
sys.stdin = open('12931_두배더하기.txt')
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
cnt = 0
while sum(nums):
    for i in range(N):
        if nums[i] % 2 == 1:
            nums[i] -= 1
            cnt += 1

    if not sum(nums):
        break

    for i in range(N):
        nums[i] //= 2
    cnt += 1

print(cnt)