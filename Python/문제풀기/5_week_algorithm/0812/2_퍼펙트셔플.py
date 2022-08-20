from collections import deque
import sys

sys.stdin = open("_퍼펙트셔플.txt")
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = input().split()
    half = N - N//2
    deque_T = deque(lst[:half])
    deque_B = deque(lst[half:])
    p_shuffle = []

    while deque_B:
        p_shuffle.append(deque_T.popleft())
        p_shuffle.append(deque_B.popleft())
    if deque_T:
        p_shuffle.append(deque_T.popleft())
    print(f'#{test_case}', *p_shuffle)