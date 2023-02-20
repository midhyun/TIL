import sys
sys.stdin = open('2644.txt')
input = sys.stdin.readline

n = int(input()) # 전체 사람 수
person_1, person_2 = map(int, input().split())
m = int(input()) # 관계 수

in_lst = [[] for _ in range(n+1)]
visited = [False]*(n+1)
chon_cnt = [0]*(n+1) 
for _ in range(m):
    i, j = map(int, input().split())
    in_lst[i].append(j)
    in_lst[j].append(i)

stack = [person_1]
visited[person_1] = True
while stack:
    man = stack.pop()                               # 사람_1
    for person in in_lst[man]:                      # 사람_1 과 인접한 사람들 리스트
        if not visited[person]:                     # 사람_1 과 인접한 사람들의 촌수는 1촌 
            visited[person] = True                  # 사람_1 = 0, 사람_1 과 인접한 사람 = 1
            chon_cnt[person] = chon_cnt[man] + 1
            stack.append(person)                    # 스택에 사람_n 을 추가
if chon_cnt[person_2] == 0:                         # 촌수가 없는 경우, -1 출력
    print(-1)
else:
    print(chon_cnt[person_2])                       # 사람_2 의 촌수를 출력
