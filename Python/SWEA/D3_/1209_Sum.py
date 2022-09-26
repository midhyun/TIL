import sys
sys.stdin = open('1209_Sum.txt')
input = sys.stdin.readline

for test_case in range(1, 11):
    case = int(input())
    graph = [[*map(int, input().split())] for _ in range(100)]
    result = 0
    for i in graph:
        result = max(result, sum(i))
    temp1 = 0
    temp2 = 0
    for i in range(100):
        temp1 += graph[i][i]
        temp2 += graph[i][-i]
    result = max(temp1, temp2, result)
    graph_col = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            graph_col[i][j] = graph[j][i]
    for i in graph_col:
        result = max(result, sum(i))
    print(f'#{test_case} {result}')
