import sys
sys.stdin = open('1216_회문2.txt')
input = sys.stdin.readline

for test_case in range(1, 11):
    n = int(input())
    graph = [[i for i in input().strip()] for _ in range(100)]
    graph_col = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            graph_col[i][j] = graph[j][i]
    result = 1
    flag = True
    for i in range(100,0,-1):
        if not flag:
            break
        for grap in graph:
            if not flag:
                break
            for j in range(100-i+1):
                x = grap[j:j+i]
                if x == x[::-1]:
                    result = max(result, i)
                    flag = False
                    break
    flag = True
    for i in range(100,0,-1):
        if not flag:
            break
        for grap in graph_col:
            if not flag:
                break
            for j in range(100-i+1):
                x = grap[j:j+i]
                if x == x[::-1]:
                    result = max(result, i)
                    flag = False
                    break
    print(f'#{test_case} {result}')