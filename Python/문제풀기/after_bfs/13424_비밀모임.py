import sys
sys.stdin = open('13424_비밀모임.txt')
input = sys.stdin.readline

t = int(input())
INF = 1e9
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    invite_n = int(input())
    invites = [*map(int, input().split())]
    dp = [[INF]*(n+1) for _ in range(invite_n)]
    for invite in invites:
        