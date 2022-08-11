import sys
sys.stdin = open('13567.txt')
input = sys.stdin.readline
M, N = map(int, input().split())
robot_pos = [0, 0]
robot_dir = 'EAST'
Move_dict = {'EAST':(0,1), 'NORTH':(1,0), 'WEST':(0,-1), 'SOUTH':(-1,0)}
matrix = [[False]*M for _ in range(M)]
valid = True

def TURN(n):
    global robot_dir
    if robot_dir == 'EAST':
        if n == 0:
            robot_dir = 'NORTH'
        else: robot_dir = 'SOUTH'
    elif robot_dir == 'WEST':
        if n == 0:
            robot_dir = 'SOUTH'
        else: robot_dir = 'NORTH'
    elif robot_dir == 'NORTH':
        if n == 0:
            robot_dir = 'WEST'
        else: robot_dir = 'EAST'
    elif robot_dir == 'SOUTH':
        if n == 0:
            robot_dir = 'EAST'
        else: robot_dir = 'WEST' 

def MOVE(n):
    global valid
    d_move = Move_dict[robot_dir]
    x = robot_pos[1] + d_move[1]*n
    y = robot_pos[0] + d_move[0]*n
    if 0 <= x < M and 0 <= y < M:
        robot_pos[1] = x
        robot_pos[0] = y
    else:
        valid = False

for i in range(N):
    order, n = input().split()
    if order == 'MOVE':
        MOVE(int(n))
    elif order == 'TURN':
        TURN(int(n))
if valid == False:
    print(-1)
else:
    print(robot_pos[1], robot_pos[0])