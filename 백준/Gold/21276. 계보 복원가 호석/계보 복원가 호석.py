import sys
from collections import deque

input = sys.stdin.readline

if __name__=="__main__":
    # 사람들의 수
    N=int(input())

    # 사람들의 이름
    people=sorted(list(map(str, input().split())))
    people_info={}  
    # {'daeil': 1, 'doha': 2, 'haeun': 3, 'hoseok': 4, 'minji': 5, 'sangdo': 6, 'yuri': 7}
    for i,p in enumerate(people):
        people_info[p]=i+1

    # 기억하는 정보의 개수 
    M=int(input())

    parents=[[] for _ in range(N+1)]    # 사람들 이름을 index로 하여 정보를 저장할 그래프 생성
    childs=[[] for _ in range(N+1)] 
    indegree=[0]*(N+1)
    for _ in range(M):
        c,p=map(str, input().split())
        # 자식의 부모를 저장
        parents[people_info[c]].append(people_info[p])
        # 부모의 자식을 저장
        childs[people_info[p]].append(people_info[c])
        # child를 가르키고 있는 조상의 수
        indegree[people_info[c]] += 1

    # 가문의 시조
    Q=deque()
    roots=[]
    res=[[] for _ in range(N+1)] 
    for p in range(1,N+1):
        # 부모가 없는 경우가 가문의 조상이다.
        if not parents[p]:
            Q.append(p)
            roots.append(people[p-1])

    # 조상의 수 출력
    print(len(roots))
    # 조상들 출력
    print(*roots)
    
    # 가문의 시조를 시작으로 내려가면서 자손들을 살펴본다
    while Q:
        x = Q.popleft()
        for child in childs[x]:     # 나(x)의 자손을 살펴봄 
            indegree[child] -= 1    # x의 자손들중 하나의 자손(child)의 조상 수를 하나 지움
            # indegree가 0으로 만드는 부모가 직계 부모이다.
            if indegree[child] == 0:        # x에 대해 indegree[child]가 0이 되었다 -> 내(x) 한세대 아래(child)
                res[x].append(people[child-1])  # x 위치에 한세대 아래 child를 넣음 
                Q.append(child)                 # 바로 아랫세대인 child를 큐에 넣어줌 

    
    for i in range(1,N+1):
        print(people[i-1], len(res[i]), *sorted(res[i]))