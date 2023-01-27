import sys
sys.stdin = open('11501_주식.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    prices = [*map(int, input().split())]
    temp = prices[-1]
    result = 0
    for i in range(n-2, -1, -1):
        if temp > prices[i]:
            result += temp - prices[i]
        else:
            temp = prices[i]
    print(result)