import sys
import heapq
sys.stdin = open('2930_힙.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    lst = []
    stack = []
    for _ in range(n):
        order = input().strip()
        if order[0] == '1':
            heapq.heappush(lst, -int(order[2:]))
        elif len(lst) == 0:
            stack.append(-1)
        else:
            stack.append(-heapq.heappop(lst))
    print(f'#{test_case}', end=' ')
    print(*stack)