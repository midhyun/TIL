import sys
sys.stdin = open('1038_감소하는수.txt')
input = sys.stdin.readline

N = int(input())
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