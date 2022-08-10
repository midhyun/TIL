import sys
sys.stdin = open('11_2.txt')
input = sys.stdin.readline

N , M = map(int, input().split())
set_lst = {input().strip() for _ in range(N)}
cnt = 0
for i in range(M):
    if input().strip() in set_lst:
        cnt += 1
print(cnt)