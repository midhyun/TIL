import sys
sys.stdin = open('15_2.txt')
input = sys.stdin.readline
# 15650_N과M
# 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열
# 고른 수열은 오름차순이여야 함

N, M = map(int, input().split())
lst = [0]
def dfs():
    if len(lst) == M+1:
        print(' '.join(map(str, lst[1:])))
        return
    for i in range(1, N+1):
        if i not in lst and i > lst[-1]:
            lst.append(i)
            dfs()
            lst.pop()
dfs()