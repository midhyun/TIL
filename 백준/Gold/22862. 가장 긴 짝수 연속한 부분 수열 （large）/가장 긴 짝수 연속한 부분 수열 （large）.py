import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = [*map(int, input().split())]

s, e = 0, 0
m_len = 0
cnt = K
while s <= e:
    if e == N:
        break

    if not (S[e] % 2):
        e += 1
    elif S[e] % 2 and cnt > 0:
        cnt -= 1
        e += 1
    elif not (S[s] % 2):
        s += 1
    elif S[s] % 2:
        s += 1
        cnt += 1
    
    m_len = max(m_len, e-s-K+cnt)

print(m_len)