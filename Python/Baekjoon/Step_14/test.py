import sys
sys.stdin = open('test.txt')

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(input().strip()) for i in range(N)] 

dy = [0, 0, -1, 1] # 동 서 남 북
dx = [1, -1, 0, 0]


stack = []
cnt = 0
for y in range(N):
    for x in range(M):                              # 그래프를 0,0 부터 순회
        if graph[y][x] == '0':                      # 물을 만났을때 !
            graph[y][x] = '1'                       # 1로 바꾸어주고 !
            cnt += 1                                # 카운트 1개 늘려주고 !
            stack.append((y, x))                    # 스택에 현재위치를 넣어줌!
            while stack:                            # 스택이 0이 될때까지 반복
                i, j = stack.pop()                  # 이제 델타 탐색으로 상하좌우가 0이면 모두 1로 변함,
                for d in range(4):                  # 인접 리스트, 즉 인접한 상하좌우 가 1로변하면서 한개의 물덩어리가 카운트되면서 방문처리가 되었으므로  
                    ny = i + dy[d]                  # 다음 순회에서 건너 뛰게 됨,
                    nx = j + dx[d]
                    if 0 <= ny < N and 0 <= nx < M: # 범위,
                        if graph[ny][nx] == '0':    # 0이면 1로 바꾸고 스택에 넣어서
                            graph[ny][nx] = '1'     # 더이상 상하좌우에 0이 없으면 종료,
                            stack.append((ny,nx))
        # 반복이 종료되면 처음 그래프 순회에서 0을 만날때 반복이 다시 시작
print(cnt)