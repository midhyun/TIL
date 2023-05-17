import sys
input = sys.stdin.readline

N = int(input())
MAX = 9876543210
cur = 0
cnt = 0
result = []
def dfs(cur):
    if len(cur) > 10:
        return

    for i in range(10):
        if int(cur[-1]) > i:
            cur += str(i)
            result.append(int(cur))
            dfs(cur)
            cur = cur.rstrip(str(i))

for i in range(10):
    result.append(i)
    dfs(str(i))

result.sort()
if len(result) > N:
    print(result[N])
else:
    print(-1)