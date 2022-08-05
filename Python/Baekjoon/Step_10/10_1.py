import sys
from collections import deque
sys.stdin = open('10_1.txt')
input = sys.stdin.readline

# 블랙잭 : 카드의 합이 21을 넘지 않는 한도 내에서 가장 합을 크게 만드는 게임
# 김정인 버전 블랙잭
# 각 카드에는 양의 정수가 쓰여 있음.
# 딜러는 N장의 카드를 숫자가 보이게 바닥에 놓음
# 딜러는 숫자 M을 크게 외침.
# N장의 카드 중에서 3장의 카드를 골라야 함.
# 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

N, M = map(int, input().split())
cards = deque(list(map(int, input().split())))
lst_sum = []
cnt = 0
for i in range(N-2):
    a = cards.popleft()
    for j in range(len(cards)-1):
        b = cards[j]
        for k in range(j+1,len(cards)):
            c = cards[k]
            d = a + b + c
            if d <= M:
                lst_sum.append(d)
            else:
                continue
print(max(lst_sum))