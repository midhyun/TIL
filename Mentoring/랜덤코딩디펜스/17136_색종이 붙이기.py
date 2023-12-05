import sys
sys.stdin = open('17136_색종이 붙이기.txt')
input = sys.stdin.readline

def solution():
    global ans
    paper = [[*map(int, input().split())] for _ in range(10)]
    counter = [0] * 6
    ans = sys.maxsize

    def sticky(y, x, length):
        for i in range(y, y + length):
            for j in range(x, x + length):
                paper[i][j] = 0

        counter[length] += 1

    def unsticky(y, x, length):
        for i in range(y, y + length):
            for j in range(x, x + length):
                paper[i][j] = 1

        counter[length] -= 1

    def checksize(y, x, length):
        for i in range(y, y + length):
            for j in range(x, x + length):
                if not paper[i][j]:
                    return False
        
        return True

    def checkall():
        for i in range(10):
            for j in range(10):
                if paper[i][j]:
                    return False
                
        return True
    
    def dfs(cnt):
        global ans
        if cnt >= ans:
            return
        if checkall():
            ans = cnt
            return
        
        for i in range(10):
            for j in range(10):
                if not paper[i][j]:
                    continue
                for length in range(5, 0, -1):
                    if counter[length] >= 5:
                        continue
                    if i+length-1 >= 10 or j+length-1 >= 10:
                        continue
                    if not checksize(i, j, length):
                        continue
                    
                    sticky(i, j, length)
                    dfs(cnt+1)
                    unsticky(i, j, length)
                return
        
    dfs(0)

    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)

solution()