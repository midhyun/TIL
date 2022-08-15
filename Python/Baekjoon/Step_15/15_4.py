import sys
sys.stdin = open('15_4.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [0]
def dfs():
    if len(lst) == M+1:
        print(' '.join(map(str, lst[1:])))
        return
    for i in range(1, N+1):
        if i >= lst[-1]:
            lst.append(i)
            dfs()
            lst.pop()
dfs()