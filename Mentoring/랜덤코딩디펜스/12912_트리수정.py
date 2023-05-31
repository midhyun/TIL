import sys
sys.stdin = open('12912_트리수정.txt')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

'''
초기에는 아무 노드에서 가장 긴 지름을 찾고
가장 긴 지름에 해당되지않는 부분 트리에서 긴 지름을 만들어서
두 트리를 이어주는 것으로 생각했지만,
가장 긴 지름이 아닌 두 부분 트리를 더한 값이 더 긴 경우가 있으므로
모든 노드를 탐색해야 함.
'''

def dfs(cur, not_node):
    visited = [-1]*N
    visited[cur] = 0
    stack = []
    stack.append(cur)

    while stack:
        cur = stack.pop()
        for nxt, dist in graph[cur]:
            if visited[nxt] == -1 and nxt != not_node:
                stack.append(nxt)
                visited[nxt] = visited[cur] + dist
    distance = max(visited)

    return (distance, visited.index(distance))



def get_diameter(N, start, not_node):

    s_node = dfs(start, not_node)[1]

    diam = dfs(s_node, not_node)[0]

    return diam

def divide_tree(root, v, parent):
    global result

    for child, dist in graph[v]:
        if child != parent:
            divide_tree(root, child, v)

            child_diam = get_diameter(N, child, v)
            root_diam = get_diameter(N, root, child)
            result = max(result, child_diam + root_diam + dist)


result = 0
divide_tree(0, 0, -1)
print(result)