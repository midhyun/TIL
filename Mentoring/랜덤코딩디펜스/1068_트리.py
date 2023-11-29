import sys
sys.stdin = open('1068_트리.txt')
input = sys.stdin.readline

N = int(input())
parents = [*map(int, input().split())]
del_node = int(input())
root_node = parents.index(-1)
parents[del_node] = -1
node = [[] for _ in range(N)]

for i in range(N):
    if parents[i] == -1:
        continue
    node[parents[i]].append(i)
node[del_node] = []

def dfs():
    visited = [False]*N
    stack = [root_node]
    visited[root_node] = True
    cnt = 0
    if root_node == del_node:
        return 0
    
    while stack:
        cur = stack.pop()
        if not node[cur]:
            cnt += 1

        for nxt in node[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
    return cnt
print(dfs())