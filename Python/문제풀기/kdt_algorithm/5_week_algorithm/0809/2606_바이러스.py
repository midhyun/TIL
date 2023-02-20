import sys
from collections import deque
sys.stdin = open('2606.txt')
input = sys.stdin.readline

n = int(input())                        # 컴퓨터의 수
edge = int(input())                     # 단선의 수
lst = [[] for _ in range(n+1)]          # 인접 리스트를 담을 빈 리스트
check = [False]*(n+1)                   # False 불리언 리스트 * 컴퓨터의 수

for _ in range(1, edge+1):              # [인접 리스트]
    i, j = map(int, input().split())    # i > j , j > i 
    lst[i].append(j)
    lst[j].append(i)
queue = deque([])                       # 큐 생성
cnt = 0                                 # 바이러스에 감염된 컴퓨터의 수
queue.append(lst[1])                    # 최초 바이러스 1번 컴퓨터의 인접리스트 값을 큐에 담아줌
while queue:
    infections = queue.popleft()        # 1번 컴퓨터와 인접한 컴퓨터들의 리스트 == 바이러스에 감염된 컴퓨터 리스트
    for i in infections:                # 인접리스트에 있는 컴퓨터들을 순회하면서 불리언값이 False 일 경우 True 로 바꾸어 주고
        if check[i] == False:           # 카운트 함.
            check[i] = True
            cnt += 1
            queue.append(lst[i])        # 감염된 컴퓨터와 인접한 컴퓨터 리스트를 큐에 넣어줌.
                                        # 큐가 0이 될때까지 반복.
            
print(cnt-1)                            # 컴퓨터 1번도 포함이므로 1을 빼줌.