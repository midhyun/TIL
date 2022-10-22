import sys
sys.stdin = open('15904_UCPC.txt')
input = sys.stdin.readline

noto = input().strip()

ucpc = 'UCPC'
idx = 0
cnt = 0
for i in noto:
    if cnt > 3:
        break
    if i == ucpc[cnt]:
        cnt += 1
        print(i)
if cnt >= 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
