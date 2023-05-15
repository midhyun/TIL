import sys
sys.stdin = open('1514_자물쇠.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
s1, s2 = input().strip(), input().strip()
a, b = [0] * 101, [0] * 101
for i in range(1, n+1):
    a[i] = int(s1[i-1])
    b[i] = int(s2[i-1])
# DP[i][i의 상태][i+1의 상태][i+2의 상태] = 최소 횟수
dp = [[[[-1]*10 for _ in range(10)] for _ in range(10)] for _ in range(101)]

def DP(now, x, y, z):
    if now > n:
        return 0
    
    ret = dp[now][x][y][z]
    if ret != -1:
        return ret
    
    ret = 1e9
    diff = (b[now] - x + 10) % 10
    d = [diff, 10 - diff]
    
    for i in range(2):
        for j in range(d[i]+1):
            for k in range(j+1):
                yy = (y + (-j if i else j) + 10) % 10
                zz = (z + (-k if i else k) + 10) % 10
                val = DP(now+1, yy, zz, a[now+3])
                val += (d[i] - j + 2) // 3 + (j - k + 2) // 3 + (k + 2) // 3
                ret = min(ret, val)
    dp[now][x][y][z] = ret
    return ret

print(DP(1, a[1], a[2], a[3]))