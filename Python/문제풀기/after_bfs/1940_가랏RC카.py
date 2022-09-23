import sys
sys.stdin = open('1940_가랏RC카.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    pos = 0
    v = 0
    for i in range(n):
        x = input().strip()
        if len(x) == 1:
            pos += v
        else:
            status, acc = map(int, x.split())
            if status == 1:
                v += acc
            elif status == 2:
                v = max(v-acc, 0)
            pos += v
    print(f'{test_case} {pos}')
