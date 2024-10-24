import sys
sys.stdin = open('15728_에리_카드.txt')
input = sys.stdin.readline
# N장의 공유, N장의 팀 카드
# 상대는 K장의 팀 카드 견제
N, K = map(int, input().split())
# 공유 카드
share_cards = sorted([*map(int, input().split())])
# 팀 카드
team_cards = sorted([*map(int, input().split())])
s, e = 0, -1
min_card, max_card = share_cards[0], share_cards[-1]
for _ in range(K):
    if max(min_card*team_cards[s], max_card*team_cards[s]) < max(min_card*team_cards[e], max_card*team_cards[e]):
        e -= 1
    else:
        s += 1

print(max(min_card*team_cards[s], max_card*team_cards[e], min_card*team_cards[e], max_card*team_cards[s]))