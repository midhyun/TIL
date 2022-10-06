import sys
sys.stdin = open('2806_N-Queen.txt')
input = sys.stdin.readline

# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
#     return True

# def n_queens(x):
#     global ans
#     if x == n:
#         ans += 1
#     else:
#         for i in range(n):
#             row[x] = i
#             if is_promising(x):
#                 n_queens(x+1)

def is_promising(x):        # x번째줄까지 놓인 퀸들과 마주보는지 확인
    for i in range(x):      # 같은 column이면 마주봄, 대각선이어도 마주봄
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False    # 마주보면 False
    return True             # 마주보지 않으면 True

def n_queens(x):
    global ans
    if x == n:                  # n번째 퀸까지 놓았다면 1개 추가
        ans += 1
    else:
        for i in range(n):      # x번째 줄에 i번째 퀸을 놓아보고
            row[x] = i
            if is_promising(x): # 이전줄들에 놓았던 퀸들과 마주보지 않으면
                n_queens(x+1)   # 다음줄에 퀸을 놓는다.

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    ans = 0
    row = [0] * n
    n_queens(0)
    print(f'#{test_case}', ans)