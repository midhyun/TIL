import sys
sys.stdin = open('7570_줄세우기.txt')
input = sys.stdin.readline

n = int(input())
children = [0] + [*map(int, input().split())]
nums = [0] * (n+1)
for i in range(1, n+1):
    nums[children[i]] = i

count = 1
max_num = 0

for i in range(1, n):
    if nums[i] < nums[i+1]:
        count += 1
        max_num = max(max_num, count)
    else:
        count = 1

print(n - max_num)