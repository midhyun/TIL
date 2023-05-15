import sys
sys.stdin = open('11502_세개의소수.txt')
input = sys.stdin.readline

def solution(cur):
    # cur 보다 작은 소수를 빼고 남은 값을 2로 나눈것이 소수이면 리턴
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
# 에라토스 테네스의 체
for i in range(2, n+1):
    if not check[i]:
        primes.append(i)
        for j in range(i+i, n+1, i):
            check[j] = True


for num in nums:
    print(*solution(num))