import sys
sys.stdin = open('21921_블로그.txt')
input = sys.stdin.readline

N, X = map(int, input().split())
visited = [0] + [*map(int, input().split())]
for i in range(1, N+1):
    visited[i] += visited[i-1]
def solution():
    tmp = 0
    tmp_lst = []
    for i in range(N-X+1):
        x = visited[i+X] - visited[i]
        if tmp <= x:
            tmp = x
            tmp_lst.append(x)

    if tmp:
        print(tmp)
        print(tmp_lst.count(tmp))
    else:
        print('SAD')

solution()