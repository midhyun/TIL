import sys
sys.stdin = open('19949_영재의시험.txt')
input = sys.stdin.readline

def dfs(score, ans):
    global result
    if len(ans) == 12:
        if score >= 5:
            result += 1
        return
    for i in range(1, 6):
        if not (ans[-1] == i and ans [-2] == i):
            ans.append(i)
            if answer[len(ans)-3] == i:
                dfs(score + 1, ans)
            else : dfs(score, ans)
            ans.pop()

answer = [*map(int, input().split())]
result = 0

dfs(0, [6, 6])
print(result)