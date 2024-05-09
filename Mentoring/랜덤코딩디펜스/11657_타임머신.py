import sys
sys.stdin = open('11657_타임머신.txt')
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    edges = []
    distance = [sys.maxsize] * (N+1)
    distance[1] = 0
    flag = True

    for _ in range(M):
        start, end, time = map(int, input().split())
        edges.append((start, end, time))
    
    for i in range(1, N+1):
        for j in range(len(edges)):
            cur, nxt, time = edges[j]
            if distance[cur] != sys.maxsize and distance[cur] + time < distance[nxt]:
                distance[nxt] = distance[cur] + time
            
                if i == N:
                    flag = False
    if not flag:
        print(-1)
        return
    
    for i in range(2, N+1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])

solution()