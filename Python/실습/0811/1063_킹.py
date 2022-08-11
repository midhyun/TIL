import sys
sys.stdin = open('1063.txt')
input = sys.stdin.readline

chess_board = [[True]*8 for _ in range(8)]
move_ ={
    'LT': (-1, -1),
    'T': (-1, 0),
    'RT': (-1, 1),
    'L': (0, -1),
    'R': (0, 1),
    'LB': (1, -1),
    'B': (1, 0),
    'RB': (1,1)
}
K, S, N = input().strip().split()
col_dic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def trans(pos): # pos = 'A1'
    col_ = col_dic[pos[0]]
    row_ = 8 - int(pos[1])
    return [row_, col_]

def trans_r(pos):
    row_ = [k for k,v in col_dic.items() if pos[1] == v]
    col_ = 8 - int(pos[0])
    result = str(*row_) + str(col_)
    return result

K_pos = trans(K)
S_pos = trans(S)
chess_board[S_pos[0]][S_pos[1]] = False

for _ in range(int(N)):
    move = move_[input().strip()]
    y = K_pos[0] + move[0]
    x = K_pos[1] + move[1]
    if 0 <= x < 8 and 0 <= y < 8:
        if not chess_board[y][x]:   # 돌이 있다면
            dy = S_pos[0] + move[0]
            dx = S_pos[1] + move[1]
            if 0 <= dx < 8 and 0 <= dy < 8: # 돌을 옮길수 있을 때,
                S_pos[0] = dy
                S_pos[1] = dx
                chess_board[y][x] = True
                chess_board[dy][dx] = False
                K_pos[0] = y
                K_pos[1] = x
        elif chess_board [y][x]:    # 돌이 없다면 왕을 이동,
            K_pos[0] = y
            K_pos[1] = x

print(trans_r(K_pos),trans_r(S_pos),sep = '\n')