import sys
sys.stdin = open('12919_A와B2.txt')
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def solution(S, T):
    if S == T:
        print(1)
        exit(0)
    if len(S) >= len(T):
        return

    if T[-1] == 'A':
        solution(S, T[:-1])
    if T[0] == 'B':
        solution(S, T[::-1][:-1])
    


solution(S, T)
print(0)