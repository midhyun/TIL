from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
queues = deque([])
lst = []
lst_origin = [*range(1,N+1)]
for i in range(M):
    n = int(input())
    queues.append([*map(int, input().split())])

for i in range(1, N+1):
    for j in range(M):
        if len(queues[j]) == 0:
            pass
        elif queues[j][-1] == i:
            lst.append(queues[j].pop())
    if len(lst) != i:
        print('No')
        break

if lst == lst_origin:
    print('Yes')