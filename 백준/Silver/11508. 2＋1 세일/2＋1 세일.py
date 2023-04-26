import sys
input = sys.stdin.readline

N = int(input())
prices = []
for _ in range(N):
    prices.append(int(input()))

prices.sort(reverse=True)
result = 0
for i in range(2, N, 3):
    tmp = prices[i-2:i+1]
    result += sum(tmp) - min(tmp)
for j in range(i+1, N):
    result += prices[j]
print(result)