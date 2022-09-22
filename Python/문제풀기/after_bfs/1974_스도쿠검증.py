import sys
sys.stdin = open('1974_스도쿠검증.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    graph = [[*map(int, input().split())]for _ in range(9)]
    flag = True
    for row in graph:
        if len(set(row)) != 9:
            flag = False
    dx = [0,1,2,0,1,2,0,1,2]
    dy = [0,0,0,1,1,1,2,2,2]
    for i in range(0,9,3):
        for j in range(0,9,3):
            box = []
            for k in range(9):
                x = j + dx[k]
                y = i + dy[k]
                box.append(graph[y][x])
            if len(set(box)) != 9:
                flag = False
    for j in range(9):
        col = []
        for i in range(9):
            col.append(graph[i][j])
        if len(set(col)) != 9:
            flag = False
    
    if not flag:
        print(f'#{test_case} 0')
    else: print(f'#{test_case} 1')