import sys
input = sys.stdin.readline

def solution(cur):
    
    for i in range(len(primes)-1, -1, -1):
        if primes[i] < cur:
            tmp = cur - primes[i]
            if tmp%2 == 0 and not check[tmp//2]:
                return (tmp//2, tmp//2, primes[i])
            
nums = []
N = int(input())
for _ in range(N):
    nums.append(int(input()))
n = max(nums)
check = [False]*(n+1)
check[0], check[1] = True, True
primes = []

for i in range(2, n+1):
    if not check[i]:
        primes.append(i)
        for j in range(i+i, n+1, i):
            check[j] = True


for num in nums:
    print(*solution(num))