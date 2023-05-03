import sys
input = sys.stdin.readline
N, K = map(int, input().split())
share_cards = sorted([*map(int, input().split())])
team_cards = sorted([*map(int, input().split())])
s, e = 0, -1
min_card, max_card = share_cards[0], share_cards[-1]

for _ in range(K):
    if max(min_card*team_cards[s], max_card*team_cards[s]) < max(min_card*team_cards[e], max_card*team_cards[e]):
        e -= 1
    else:
        s += 1

print(max(min_card*team_cards[s], max_card*team_cards[e], min_card*team_cards[e], max_card*team_cards[s]))