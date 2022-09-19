import sys
sys.stdin = open('D2_1976.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())
    m = m1 + m2
    h = h1 + h2
    if 60 <= m:
        h += 1
        m -= 60
    if 13 <= h:
        h -= 12
    print(f'#{test_case} {h} {m}')