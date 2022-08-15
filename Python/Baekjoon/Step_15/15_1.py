import sys
sys.stdin = open('15_1.txt')
input = sys.stdin.readline
# 백트래킹 - 
# 15649_N과 M(1)

N, M = map(int, input().split())

#길이가 M인 수열을 모두 구하는 프로그램?
# 1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열
# N개에서 M개 고른 ?
# 경우의 수 = N!/M!
# 재귀하면서 조건에서 해를 출력하고,
# pop으로 한칸 되돌아 간후에 다음 반복문으로 진행,
line = []
def dfs():
    if len(line) == M:
        print(' '.join(map(str,line)))
        return
    for i in range(1, N+1):
        if i not in line:
            line.append(i)
            dfs()
            line.pop()

dfs()