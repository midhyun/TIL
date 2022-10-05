from re import L
import sys
sys.stdin = open('6485_삼성시의버스노선.txt')
sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    stops = [0]*5001
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            stops[i] += 1
    p = int(input())
    result = []
    for _ in range(p):
        c = int(input())
        result.append(stops[c])
    print(f'#{test_case}', *result)