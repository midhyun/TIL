import sys
sys.stdin = open('1475_방 번호.txt')
input = sys.stdin.readline

nums = [0]*10
N = input().strip()

for i in N:
    nums[int(i)] += 1
result = 0
nums[6] += nums[9]
for i in range(9):
    num = nums[i]
    if num == 0:
        continue
    if i == 6:
        if num % 2 == 1:
            num = (num+1)//2
        else:
            num //= 2
    result = max(result, num)
print(result)