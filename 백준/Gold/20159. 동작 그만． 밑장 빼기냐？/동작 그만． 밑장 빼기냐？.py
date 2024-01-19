import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    cards = [*map(int, input().split())]
    prefix_sum = [0]*N
    
    for i in range(-2, -N-1, -2):
        prefix_sum[i] = prefix_sum[i+2] + cards[i]

    ans = prefix_sum[0]
    sum_cards = prefix_sum[0]

    for i in range(N-1, 0, -2):
        sum_cards += cards[i]
        sum_cards -= cards[i-1]
        ans = max(ans, sum_cards)
    
    sum_cards = prefix_sum[0]

    for i in range(N-2, 1, -2):
        sum_cards -= cards[i]
        sum_cards += cards[i-1]
        ans = max(ans, sum_cards)

    print(ans)


solution()