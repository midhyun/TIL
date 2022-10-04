graph = [[0]*6 for _ in range(6)]
cnt = 1
for i in range(2, 7):
    for j in range(1, i):
        graph[i-j][j] = cnt
        cnt += 1
for i in range(2, 6):
    for j in range(i,6):
        graph[5+i-j][j] = cnt
        cnt += 1
for grap in graph:
    print(grap)