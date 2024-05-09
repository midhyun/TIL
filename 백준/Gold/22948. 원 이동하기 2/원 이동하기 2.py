import sys
import heapq
input = sys.stdin.readline

def solution():
    def backt(cnt, cur):
        if cur == end:
            print(cnt)
            for num in path:
                print(num, end=' ')
            return
        
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = 1
                path.append(nxt)
                backt(cnt+1, nxt)
                path.pop()
                visited[nxt] = -1
    
    N = int(input())
    circles = []

    for _ in range(N):
        k, x, r = map(int, input().split())
        circles.append((x-r, k))
        circles.append((x+r, -k))

    start, end = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    visited = [-1]*(N+1)
    heapq.heapify(circles)

    stack = [0]
    while circles:
        x, num = heapq.heappop(circles)
        if num < 0:
            stack.pop()
        else:
            graph[num].append(stack[-1])
            graph[stack[-1]].append(num)
            stack.append(num)

    visited[start] = True
    path = [start]
    backt(1, start)

solution()