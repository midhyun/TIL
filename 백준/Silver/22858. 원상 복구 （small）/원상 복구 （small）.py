import sys
input = sys.stdin.readline

def Reverse_string(x):
    cur_S = x
    for _ in range(K):
        tmp = [0]*N
        for i in range(N):
            tmp[i] = cur_S[Rev_D[i]-1]
        cur_S = tmp
    return cur_S

N, K = map(int, input().split())
S = [*map(int, input().split())]
D = [*map(int, input().split())]

Rev_D = [0]*N
for i in range(1, N+1):
    Rev_D[D[i-1]-1] = i



print(*Reverse_string(S))