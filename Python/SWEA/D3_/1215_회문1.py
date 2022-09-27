import sys
sys.stdin = open('1215_회문1.txt')
input = sys.stdin.readline

for test_case in range(1, 11):
    n = int(input())
    graph = [[i for i in input().strip()] for _ in range(8)]
    graph_col = [[0]*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            graph_col[i][j] = graph[j][i]
    cnt = 0
    for grap in graph:
        for i in range(8-n+1):
            x = grap[i:i+n]
            if x == x[::-1]:
                cnt += 1
    for grap in graph_col:
        for i in range(8-n+1):
            x = grap[i:i+n]
            if x == x[::-1]:
                cnt += 1
    print(f'#{test_case} {cnt}')