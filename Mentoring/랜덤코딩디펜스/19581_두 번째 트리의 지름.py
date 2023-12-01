import sys
sys.stdin = open('19581_두 번째 트리의 지름.txt')
input = sys.stdin.readline

def solution():
    N = int(input())
    node = [[] for _ in range(N+1)]
    for _ in range(N-1):
        i, j, d = map(int, input().split())
        node[i].append((j, d))
        node[j].append((i, d))
    def dfs(far, rmv = 0):
        distList = []
        visited = [False]*(N+1)
        stack = [(far, 0)]
        visited[far] = True
        visited[rmv] = True
        while stack:
            cur, curDist = stack.pop()
            for nxt, dist in node[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    nxtDist = curDist + dist
                    stack.append((nxt, nxtDist))
                    distList.append((nxtDist, nxt))
        distList.sort(reverse=True)
        return distList
    # 가장 끝 점
    farDist, far = dfs(1)[0]
    # 끝 점에서 지름
    farDist, far1 = dfs(far)[0]
    print(max(dfs(far, far1)[0][0], dfs(far1, far)[0][0]))


solution()