import sys
sys.stdin = open('7682_틱택토.txt')
input = sys.stdin.readline

def check():
    board = input().strip()
    if board == 'end':
        return False
    x_cnt = board.count('X')
    o_cnt = board.count('O')
    empty_cnt = board.count('.')
    x_win = False
    o_win = False
    if not(x_cnt == o_cnt or x_cnt == o_cnt + 1):
        return 'invalid'
    
    #가로
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != '.':
            if board[i] == 'X' and not x_win:
                x_win = True
            elif board[i] == 'O' and not o_win:
                o_win = True

    
    #세로
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != '.':
            if board[i] == 'X' and not x_win:
                x_win = True
            elif board[i] == 'O' and not o_win:
                o_win = True

    
    #대각선
    if board[0] == board[4] == board[8] != '.':
        if board[0] == 'X' and not x_win:
            x_win = True
        elif board[0] == 'O' and not o_win:
            o_win = True

    if board[2] == board[4] == board[6] != '.':
        if board[2] == 'X' and not x_win:
            x_win = True
        elif board[2] == 'O' and not o_win:
            o_win = True

    #체크
    if x_win and o_win:
        return 'invalid'
    elif (x_cnt - o_cnt) == 1 and x_win:
        return 'valid'
    elif (x_cnt == o_cnt) and o_win:
        return 'valid'
    elif (x_cnt == 5) and (o_cnt == 4) and not x_win and not o_win:
        return 'valid'     
    else:
        return 'invalid'
while True:
    chk = check()
    if not chk:
        break
    print(chk)