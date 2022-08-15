import sys
sys.stdin = open('15_3.txt')
input = sys.stdin.readline
# 15651_N과M(3)

N, M = map(int, input().split())
lst = []
def dfs():
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return
    for i in range(1, N+1):
        lst.append(i)
        dfs()
        lst.pop()
dfs()