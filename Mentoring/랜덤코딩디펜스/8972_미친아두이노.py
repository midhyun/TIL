import sys
sys.stdin = open('8972_미친아두이노.txt')
input = sys.stdin.readline

dy, dx = [1, 1, 1, 0, 0, 0, -1, -1, -1], [-1, 0, 1, -1, 0, 1, -1, 0, 1]

def solution():
    r, c = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(r)]
    moves = input().rstrip()
    mad_robots = set()
    jong = ()

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                mad_robots.add((i, j))
            if board[i][j] == 'I':
                jong = (i, j)
    
    for m_num in range(len(moves)):
        # 종수이동
        ny, nx = jong[0] + dy[int(moves[m_num])-1], jong[1] + dx[int(moves[m_num])-1]
        if board[ny][nx] == 'R':
            return (False, m_num+1)
        board[jong[0]][jong[1]] = '.'
        jong = (ny, nx)
        board[ny][nx] = 'I'
        distroyed = set()
        nxt_robots = set()

        # 미친로봇이동
        visited = [[False]*c for _ in range(r)]
        for i, j in mad_robots:
            min_d = sys.maxsize
            nxt_pos = ()
            # 거리가 가까운쪽으로 이동
            for n in range(9):
                ny, nx = i + dy[n], j + dx[n]
                if 0 <= ny < r and 0 <= nx < c:
                    dist = (abs(jong[0] - ny) + abs(jong[1] - nx))
                    if dist < min_d:
                        min_d = dist
                        nxt_pos = (ny, nx)
            # 조건검사
            if board[nxt_pos[0]][nxt_pos[1]] == 'I':
                return (False, m_num+1)
            elif visited[nxt_pos[0]][nxt_pos[1]]:
                distroyed.add((nxt_pos[0], nxt_pos[1]))
            visited[nxt_pos[0]][nxt_pos[1]] = True
            nxt_robots.add(nxt_pos)

        for i, j in distroyed:
            board[i][j] = '.'
            nxt_robots.discard((i, j))
        
        for i, j in mad_robots:
            board[i][j] = '.'
        for i, j in nxt_robots:
            board[i][j] = 'R'
        mad_robots = nxt_robots
    
    for b in board:
        print("".join(b))
    return (True, 0)

result = solution()
if not result[0]:
    print(f'kraj {result[1]}')