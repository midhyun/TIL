import sys
input = sys.stdin.readline

def solution():
    while True:
        N, K = map(int, input().split())
        if N == 0 and K == 0:
            break
        arr = [*map(int, input().split())]
        children = [[] for _ in range(arr[-1]+1)]
        parents = [i for i in range(arr[-1]+1)]
        parent = -1
        for i in range(1, N):
            if arr[i] != arr[i-1]+1:
                parent += 1
            children[arr[parent]].append(arr[i])
            parents[arr[i]] = arr[parent]
        result = 0
        if parents[K] == parents[parents[K]]:
            print(0)
            continue
        for num in children[parents[parents[K]]]:
            if num != parents[K]:
                result += len(children[num])
        
        print(result)

    return

solution()
