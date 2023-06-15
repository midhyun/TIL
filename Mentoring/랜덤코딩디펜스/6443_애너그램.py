import sys
sys.stdin = open('6443_애너그램.txt')
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())


def dfs(cur):
    if cur == len(word):
        print(''.join(answer))
        return

    for k in visited:
        if visited[k]:
            visited[k] -= 1
            answer.append(k)
            dfs(cur+1)
            visited[k] += 1
            answer.pop()
    
for word in words:
    word = sorted(list(word))
    visited = {}
    answer = []
    for i in word:
        visited[i] = visited.get(i, 0) + 1

    dfs(0)