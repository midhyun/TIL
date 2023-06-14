import sys
sys.stdin = open('16508_전공책.txt')
input = sys.stdin.readline

T = input().rstrip()
N = int(input())
titles = []
prices = []
for _ in range(N):
    price, title = input().split()
    prices.append(int(price))
    titles.append(title)
graph = [[] for _ in range(len(T))]

def find(cur):
    for i in range(N):
        for j in range(len(titles[i])):
            if T[cur] == titles[i][j]:
                graph[cur].append((i, j))

for i in range(len(T)):
    find(i)
INF = sys.maxsize
result = INF
bit = [0]*N
def dfs(cur, bit):
    global result
    if cur == len(T):
        tmp = 0
        for b in range(N):
            if bit[b]:
                tmp += prices[b]
        result = min(result, tmp)
        return
    
    for n, j in graph[cur]:
        if not (bit[n] & (1<<j)):
            bit[n] ^= 1<<j
            dfs(cur+1, bit)
            bit[n] ^= 1<<j

dfs(0, bit)
if result == INF:
    print(-1)
else:
    print(result)