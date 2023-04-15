import sys
sys.stdin = open('20365_블로그2.txt')
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

def solution():
    cur = None
    cnt_B = 0
    cnt_R = 0
    for i in range(N):
        if S[i] != cur:
            cur = S[i]
            if S[i] == 'B':
                cnt_B += 1
            else:
                cnt_R += 1

    if S[0] == 'B':
        return cnt_R + 1
    else:
        return cnt_B + 1

print(solution())