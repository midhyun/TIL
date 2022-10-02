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
    for i in range(100,0,-1):                   # 100 , 99 , 98, ... 문자열의 길이
        if not flag:
            break
        for grap in graph:                      # 그래프의 첫번째 줄
            if not flag:
                break
            for j in range(100-i+1):            # 길이만큼나오는 개수 0부터 가는데 
                x = grap[j:j+i]
                if x == x[::-1]:                # x가 회문인가 ? 회문은 인도인 별똥별 스위스 기러기 토마토 우영우
                    result = max(result, i)     # 회문이다 !
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
                    result = max(result, i)     # 가로로 찾은 회문의 최대길이와 세로로 찾은 회문의 최대길이
                    flag = False
                    break
    print(f'#{test_case} {result}')