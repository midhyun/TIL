import sys
sys.stdin = open('11724.txt')
input = sys.stdin.readline

# 인접 리스트 생성
N, M = map(int, input().split())
in_line = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    i, j = map(int, input().split())
    in_line[i].append(j)
    in_line[j].append(i)

                                            # 서로 연결요소일 경우, 반복문을 통해 방문처리가 됨,
cnt = 0                                     # 연결요소가 아닐 경우 아직 미방문임
for i in range(1, N+1):                     # 모든 노드를 순회함.
    if visited[i] == False:                 # 방문처리가 안된 노드일 경우 카운트, 방문처리를 했을 경우 노카운트
        cnt += 1                            
    elif sum(visited) == N:                 # 모든 노드를 방문 했다면, 반복 종료,
        break
    else:
        pass
    stack = []
    visited[i] = True
    stack.append(in_line[i])                # 스택에 i의 인접리스트를 추가함
    while stack:                            # 스택에 요소가 없을 때까지 반복
        nodes = stack.pop()                 # 인접 리스트
        for node in nodes:                  # 인접 리스트를 순회함
            if not visited[node]:           # 방문한 적이 없다면 
                visited[node] = True        # 방문처리
                stack.append(in_line[node]) # 방문한 노드의 인접노드리스트를 스택에 추가
    
print(cnt)
