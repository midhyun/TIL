import sys
sys.stdin = open('5533.txt')
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]    # 행렬 만들어주고
matrix_check = [[True]*3 for _ in range(n)]                     # 체크 용 행렬
# score = []
for k in range(3):
    game_nums = [matrix[j][k] for j in range(n)]
    for i in range(n):                                          # 중복값이 있을경우
        if game_nums.count(matrix[i][k]) > 1:                   # count가 2 이상일 경우 중복된 값임
            matrix_check[i][k] = False                          # 체크 배열에 False 체크
            # score.append(matrix[i][k])
for i in range(3):
    for j in range(n):
        if matrix_check[j][i] == False:                         # 체크 배열에서 False 일 경우 0점
            matrix[j][i] = 0                                    # True일 경우 숫자가 곧 점수
for i in range(n):
    print(sum(matrix[i]))                                       # 각 행의 값을 더해줌 플레이어의 점수가 출력되도록