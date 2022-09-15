import sys
from collections import deque
sys.stdin = open('5430_AC.txt')
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    order = input().strip()
    n = int(input())
    arr = input()
    if n == 0:
        arr = deque([])
    else:
        arr = deque(arr.strip()[1:-1].split(','))

    rev = False
    for i in order:
        if i == 'R':
            if rev:
                rev = False
            else: rev = True
        elif i == 'D':
            if len(arr) == 0:
                print('error')
                break
            if not rev:
                arr.popleft()
            elif rev:
                arr.pop()
    else:
        if rev:
            arr.reverse()
            print('[' + ','.join(arr) + ']')
        elif not rev:
            print('[' + ','.join(arr) + ']')