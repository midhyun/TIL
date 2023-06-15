import sys
sys.stdin = open('6443_애너그램.txt')
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())


def dfs(visited, cur):
    if len(cur) >= len(visited):
        tmp.add(cur)
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            dfs(visited, cur+word[i])
            visited[i] = False
    
for word in words:
    visited = [False]*len(word)
    tmp = set()
    dfs(visited, '')
    for x in sorted(list(tmp)):
        print(x)