from collections import deque

T = int(input())
cards_deq = deque([*range(1, T+1)])
tomb = []

for test_case in range(1, T):
    tomb.append(cards_deq.popleft())
    cards_deq.append(cards_deq.popleft())

print(*tomb,*cards_deq,sep=' ')