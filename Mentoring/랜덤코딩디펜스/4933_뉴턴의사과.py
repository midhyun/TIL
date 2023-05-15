import sys
sys.stdin = open('4933_뉴턴의사과.txt')
input = sys.stdin.readline

N = int(input())
# (뒤집어서) A의 자식이 있으면 값이나옴, 없으면 nil, 왼쪽오른쪽 둘다있거나 하나만있거나, 둘다없거나
for _ in range(N):
    fst_graph = [[] for _ in range(27)]
    sec_graph = [[] for _ in range(27)]
    fst_ = input().split()
    sec_ = input().split()
    fst_.pop(), sec_.pop()

    parent = [ord(fst_.pop()) - 65]
    cnt = 0
    visited1 = [0]*27
    while parent:
        if not fst_:
            break
        
        if visited1[parent[-1]] >= 2:
            parent.pop()
            continue

        p = fst_.pop()
        if p == 'nil':
            visited1[parent[-1]] += 1
            continue

        visited1[parent[-1]] += 1
        fst_graph[parent[-1]].append(p)
        parent.append(ord(p) - 65)
    
    parent = [ord(sec_.pop()) - 65]
    cnt = 0
    visited = [0]*27
    while parent:
        if not sec_:
            break
        
        if visited[parent[-1]] >= 2:
            parent.pop()
            continue

        p = sec_.pop()
        if p == 'nil':
            visited[parent[-1]] += 1
            continue

        visited[parent[-1]] += 1
        sec_graph[parent[-1]].append(p)
        parent.append(ord(p) - 65)
        

    for i in range(len(fst_graph)):
        fst_graph[i] = sorted(fst_graph[i])
    for i in range(len(sec_graph)):
        sec_graph[i] = sorted(sec_graph[i])

    if fst_graph == sec_graph:
        print('true')
    else:
        print('false')