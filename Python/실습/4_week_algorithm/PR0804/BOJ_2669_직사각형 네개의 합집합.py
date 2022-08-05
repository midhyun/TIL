import sys
sys.stdin = open('2669.txt')
input = sys.stdin.readline
board = [[False]*100 for i in range(100)]                           # False 100 x 100 보드

for _ in range(4):
    x_left, y_left ,x_right ,y_right = map(int, input().split())
    
    for i in range(y_left, y_right):                                # False 보드에 해당 범위를 True로 체크해줌
        for j in range(x_left, x_right):
            board[i][j] = True
    
cnt = 0
for i in range(100):                                                # 100 x 100 False 보드에서 True의 갯수를 세어줌 == 면적
    for j in range(100):
        if board[i][j] == True:
            cnt += 1
print(cnt)