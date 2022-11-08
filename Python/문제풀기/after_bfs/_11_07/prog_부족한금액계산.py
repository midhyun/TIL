import sys
sys.stdin = open('prog_부족한금액계산.txt')
input = sys.stdin.readline

price, money, count, result = 3, 20, 4, 10

price_sum = 0
for i in range(1, count+1):
    price_sum += price*i


if price_sum > money:
    print( price_sum - money)
else:
    print(0)