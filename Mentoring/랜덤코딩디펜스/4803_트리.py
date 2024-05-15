import sys
sys.stdin = open('4803_트리.txt')
input = sys.stdin.readline

def solution():
    case = 0
    while True:
        case += 1
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            exit()

        graph = [[] for _ in range(N + 1)]
        visited = [False] * (N + 1)

        for _ in range(M):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, parent):
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                if visited[nxt]:
                    return False
                visited[nxt] = True
                if not dfs(nxt, node):
                    return False
            return True

        trees = 0
        for i in range(1, N +1):
            if not visited[i]:
                visited[i] = True
                if dfs(i, 0):
                    trees += 1
        
        if trees == 0:
            print(f"Case {case}: No trees.")
        elif trees == 1:
            print(f"Case {case}: There is one tree.")
        else:
            print(f"Case {case}: A forest of {trees} trees.")

solution()