import sys
sys.stdin = open('2805_농작물수확하기.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    graph = [[int(i) for i in list(input().strip())] for _ in range(n)]
    cnt = 0
    h = (n//2)
    for i in range(h+1):
        for j in range(h-i,h+i+1):
            cnt += graph[j][i]

    for i in range(h):
        for j in range(h-i,h+i+1):
            cnt += graph[-j-1][-i-1]
    print(f'#{test_case} {cnt}')