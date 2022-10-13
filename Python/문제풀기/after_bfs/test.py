import sys
from collections import deque
sys.stdin = open('1726_로봇.txt')
input = sys.stdin.readline

def turn_left(direction):
    turn_dir = (3, 2, 0, 1)
    return turn_dir[direction]


def turn_right(direction):
    turn_dir = (2, 3, 1, 0)
    return turn_dir[direction]

n, m = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]

s_pos = [*map(int, input().split())]
e_pos = [*map(int, input().split())]
for i in range(3):
    s_pos[i] -= 1
    e_pos[i] -= 1
s_y, s_x, s_d = s_pos
e_y, e_x, e_d = e_pos

visited = [[[0]*4 for _ in range(m)] for _ in range(n)]
visited[s_y][s_x][s_d] = 1

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

q = deque()
q.append((s_y, s_x, s_d))

while q:
    if visited[e_y][e_x][e_d]:
        break
    cur_y, cur_x, cur_d = q.popleft()
    y, x = cur_y, cur_x
    for _ in range(3):
        y += dy[cur_d]
        x += dx[cur_d]
        if y < 0 or y >= n or x < 0 or x >= m or graph[y][x]:
            break
        if visited[y][x][cur_d]:
            continue
        visited[y][x][cur_d] = visited[cur_y][cur_x][cur_d] + 1
        q.append((y, x, cur_d))
    left_turn = turn_left(cur_d)
    right_turn = turn_right(cur_d)

    for dir in (left_turn, right_turn):

        if not visited[cur_y][cur_x][dir]:
            visited[cur_y][cur_x][dir] = visited[cur_y][cur_x][cur_d] + 1
            q.append((cur_y, cur_x, dir))

print(visited[e_y][e_x][e_d] - 1)
