import sys
sys.stdin = open('1873_상호의배틀필드.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    h, w = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    n = int(input())
    orders = list(input().strip())
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '<' or graph[i][j] == '>' or graph[i][j] == '^' or graph[i][j] == 'v':
                pos = [i, j]
                break
    for order in orders:
        if order == 'S':
            if graph[pos[0]][pos[1]] == '^':
                for i in range(pos[0]-1, -1, -1):
                    if graph[i][pos[1]] == '*':
                        graph[i][pos[1]] = '.'
                        break
                    elif graph[i][pos[1]] == '#':
                        break
            elif graph[pos[0]][pos[1]] == 'v':
                for i in range(pos[0]+1, h):
                    if graph[i][pos[1]] == '*':
                        graph[i][pos[1]] = '.'
                        break
                    elif graph[i][pos[1]] == '#':
                        break
            elif graph[pos[0]][pos[1]] == '<':
                for i in range(pos[1]-1, -1, -1):
                    if graph[pos[0]][i] == '*':
                        graph[pos[0]][i] = '.'
                        break
                    elif graph[pos[0]][i] == '#':
                        break
            elif graph[pos[0]][pos[1]] == '>':
                for i in range(pos[1]+1, w):
                    if graph[pos[0]][i] == '*':
                        graph[pos[0]][i] = '.'
                        break
                    elif graph[pos[0]][i] == '#':
                        break
        elif order == 'U':
            graph[pos[0]][pos[1]] = '.'
            if  0 <= pos[0]-1 < h and graph[pos[0]-1][pos[1]] == '.' :
                pos[0] -= 1
            graph[pos[0]][pos[1]] = '^'
        elif order == 'D':
            graph[pos[0]][pos[1]] = '.'
            if 0 <= pos[0]+1 < h and graph[pos[0]+1][pos[1]] == '.':
                pos[0] += 1
            graph[pos[0]][pos[1]] = 'v'
        elif order == 'L':
            graph[pos[0]][pos[1]] = '.'            
            if 0 <= pos[1]-1 < w and graph[pos[0]][pos[1]-1] == '.':
                pos[1] -= 1
            graph[pos[0]][pos[1]] = '<'
        elif order == 'R':
            graph[pos[0]][pos[1]] = '.'
            if 0 <= pos[1]+1 < w and graph[pos[0]][pos[1]+1] == '.':
                pos[1] += 1
            graph[pos[0]][pos[1]] = '>'
    print(f'#{test_case}', end=' ')
    for grap in graph:
        print(''.join(grap))