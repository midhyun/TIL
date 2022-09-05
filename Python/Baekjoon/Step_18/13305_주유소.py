import sys
sys.stdin = open('13305_주유소.txt')
input = sys.stdin.readline

n = int(input())
road = [*map(int, input().split())] # n -1
oil_price = [*map(int, input().split())] # n

cur = oil_price[0]
result = 0
for i in range(n-1):
    cur = min(cur, oil_price[i])
    result += road[i]*cur

print(result)