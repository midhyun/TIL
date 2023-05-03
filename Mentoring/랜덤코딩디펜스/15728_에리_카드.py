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
    if share_cards[0]*team_cards[s] < share_cards[-1]*team_cards[e]:
        e -= 1
    else:
        s += 1

print(max(share_cards[0]*team_cards[s], share_cards[-1]*team_cards[e]))