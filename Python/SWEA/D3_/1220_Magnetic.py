import sys
sys.stdin = open('1220_Magnetic.txt')
input = sys.stdin.readline

for test_case in range(1, 11):
    n = int(input())
    graph = [[*map(int, input().split())] for _ in range(100)]
    graph_col = [[False]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            graph_col[i][j] = graph[j][i]

    cnt = 0
    for i in range(100):
        temp = 0
        for j in range(100):
            if temp == 0 and graph_col[i][j] == 1:
                temp = 1
            if temp == 1 and graph_col[i][j] == 2:
                temp = 0
                cnt += 1
    print(f'#{test_case} {cnt}')