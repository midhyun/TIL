import sys
sys.stdin = open('1541_잃어버린괄호.txt')
input = sys.stdin.readline

all = input().strip()
nums = all.split('-')
result = 0
start = nums[0].split('+')

for num in start:
    result += int(num)
for num in nums[1:]:
    minuses = num.split('+')
    for minus in minuses:
        result -= int(minus)
print(result)