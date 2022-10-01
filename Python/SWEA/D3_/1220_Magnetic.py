import sys
sys.stdin = open('1220_Magnetic.txt')
input = sys.stdin.readline
# 테이블 위에 자석들이 놓여져 있음
# 테이블의 위로 N극 아래로 S극
# 특수한 자성체 조건, 힘의 합력은 고려하지 않음 
# N극과 S극이 부딪힌 순간 정지하고 속력도 한칸씩
# 빨간색 아래에 파란색이 있으면 떨어지지 못함.
# 파란색 위에 빨간색이 있으면 떨어지지 못함. 
# 빨간색 또는 기준으로 그래프 순회를 하면 됨
# 그래프를 순회하면서 빨간색이 올려져 있는 coloumn 에서
# column 값이 더 큰 칸중에 파란색이 올려져 있다면 빨간색은 떨어지지 않음
# 즉, 떨어지지 않는 빨강파랑 한쌍이 생김
# 빨빨파 인 경우에도 한쌍임
# 즉, 빨강밑에 빨강이면 패스, 카운트하지않고 파랑일때 카운트
# 



for test_case in range(1, 11):
    n = int(input())
    graph = [[*map(int, input().split())] for _ in range(100)] # 입력받은 그래프
    graph_col = [[False]*100 for _ in range(100)]              # 전치 그래프 y x 를 바꿈
    for i in range(100):
        for j in range(100):
            graph_col[i][j] = graph[j][i]                       # 그래프 전치

    cnt = 0
    for i in range(100):                                        # 그래프 순회
        temp = 0                                                # 쌍확인을 위한 변수
        for j in range(100):
            if temp == 0 and graph_col[i][j] == 1:              # 현재 그래프의 값이 빨간색 이고, temp가 초기값일때
                temp = 1                                        # temp = 1 을 해주어서 현재 빨간색하나가 대기상태임
            if temp == 1 and graph_col[i][j] == 2:              # 빨간색 밑에 파란색이 있는 경우!
                temp = 0                                        # 대기중인 빨간색은 쌍이되었으므로 temp 초기화
                cnt += 1                                        # 빨강파랑 쌍 갯수 카운트 !
    print(f'#{test_case} {cnt}')