import sys
sys.stdin = open('2798.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(n-2):
    if result == m:
        break
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum_cards = cards[i] + cards[j] + cards[k]

            if sum_cards <= m and sum_cards >= result:
                result = sum_cards

print(result)