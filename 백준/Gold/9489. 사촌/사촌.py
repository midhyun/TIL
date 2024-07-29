import sys
from collections import defaultdict
input = sys.stdin.readline

def solution2():
    while True:
        N, K = map(int, input().split())
        if (N, K) == (0, 0):
            break

        arr = [*map(int, input().split())]
        parent = defaultdict(int)

        idx = -1
        for i in range(1, N):
            if arr[i] != arr[i-1]+1:
                idx += 1
            parent[arr[i]]= arr[idx]
        
        cnt = 0
        if parent[parent[K]]:
            for node in arr:
                if (parent[parent[K]] == parent[parent[node]]) and parent[node] != parent[K]:
                    cnt += 1
        
        print(cnt)

solution2()

