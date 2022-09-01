import sys
sys.stdin = open('2559_수열.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
nums =[0]+[*map(int, input().split())]
for i in range(1,n+1):
    nums[i] += nums[i-1]

stack = []

for i in range(k,n+1):
    stack.append(nums[i]-nums[i-k])

print(max(stack))