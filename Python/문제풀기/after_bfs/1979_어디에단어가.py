import sys
sys.stdin = open('1979_어디에단어가.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    graph_row = [[*map(int, input().split())] for _ in range(n)]
    graph_col = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            graph_col[j][i] = graph_row[i][j]
    cnt = 0
    for i in graph_row:
        temp = ''
        for j in [*map(str, i)]:
            temp += j
        temp = temp.split('0')
        for x in temp:
            if len(x) == k:
                cnt += 1
    for i in graph_col:
        temp = ''
        for j in [*map(str, i)]:
            temp += j
        temp = temp.split('0')
        for x in temp:
            if len(x) == k:
                cnt += 1
    print(f'#{test_case} {cnt}')