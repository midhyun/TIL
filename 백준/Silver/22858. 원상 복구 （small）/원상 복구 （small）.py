import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = [*map(int, input().split())]
D = [*map(int, input().split())]

Rev_D = [0]*N
for i in range(1, N+1):
    Rev_D[D[i-1]-1] = i

cur_S = S
for _ in range(K):
    tmp = [0]*N
    for i in range(N):
        tmp[i] = cur_S[Rev_D[i]-1]
    cur_S = tmp

print(*cur_S)