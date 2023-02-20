import sys
sys.stdin = open('2606.txt')
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    i, j = map(int, input().split())
    lst[i].append(j)
    lst[j].append(i)

def dfs(start):
    stack = [start]                     # 초기 값, 시작 노드, 감염된 1번 컴퓨터
    visited[start] = True               # 이후 감염된 컴퓨터들을 스택에 추가해서 연결된 컴퓨터들을 감염시킴
    cnt = 0
    while stack:                        # 스택의 요소가 없을 때 까지 반복
        infects = stack.pop()           # 스택에 추가된 감염된 컴퓨터들
        for infect in lst[infects]:     # 감염된 컴퓨터(infects)의 인접 리스트를 순회함
            if not visited[infect]:     # 감염된 컴퓨터와 인접하므로 감염됨, 
                visited[infect] = True  # 감염처리가 안되어 있었으므로 감염처리
                stack.append(infect)    # 감염 되었으므로 스택에 추가,
                cnt += 1                # 감염된 컴퓨터의 수 +1
    return cnt                          # 감염된 컴퓨터의 수를 반환함.
print(dfs(1))