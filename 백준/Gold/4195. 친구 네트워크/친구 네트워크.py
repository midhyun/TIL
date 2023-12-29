import sys
input = sys.stdin.readline

def solution():

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return
        else:
            parent[y] = x
            visited[x] += visited[y]
    
    def find(target):
        if target == parent[target]:
            return target
        else:
            parent[target] = find(parent[target])
            return parent[target]
    

    TESTCASE = int(input())
    for t in range(TESTCASE):
        NETWORK = int(input())
        parent = dict()
        visited = dict()
        for f in range(NETWORK):
            a, b = input().split()

            if a not in parent:
                parent[a] = a
                visited[a] = 1
            
            if b not in parent:
                parent[b] = b
                visited[b] = 1

            union(a, b)
            print(visited[find(a)])

solution()