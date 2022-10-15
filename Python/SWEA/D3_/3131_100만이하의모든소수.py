import sys
sys.stdin = open('3131_100만이하의모든소수.txt')
input = sys.stdin.readline

n = 1000000
x = int(n**(1/2))+1
nums = [True] * (n+1)
nums[0] = False
nums[1] = False
for i in range(2, x):
    if nums[i] == True:
        for j in range(i+i,n+1,i):
            nums[j] = False

for i in range(n+1):
    if nums[i] == True:
        print(i, end=' ')