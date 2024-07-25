import sys
sys.stdin = open('16202_MST게임.txt')
input = sys.stdin.readline

def solution():
    N, M, K = map(int, input().split())
    edges = []
    for i in range(M):
        a, b = map(int, input().split())
        edges.append((i+1, a, b))
        edges.append((i+1, b, a))

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)

        if a < b: parent[b] = a
        else: parent[a] = b
    result = []
    flag = True
    for i in range(K):
        parent = [ i for i in range(N+1)]
        value = 0
        edge_cnt = 0

        if not flag:
            result.append(value)
            continue
        for edge in edges[i*2:]:
            cost, a, b = edge
            if find(parent, a) != find(parent, b):
                union(parent, a, b)
                value += cost
                edge_cnt += 1
        if edge_cnt != N-1:
            result.append(0)
            flag = False
        else:
            result.append(value)

    print(*result)

    return

solution()
