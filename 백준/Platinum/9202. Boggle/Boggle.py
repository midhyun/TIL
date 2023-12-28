import sys
input = sys.stdin.readline

def solution():
    def dfs(i, j, cur):
        if len(cur) > 8:
            return
        if cur in word_dict:
            word_dict[cur] = 1

        for k in range(8):
            y, x = i + dy[k], j + dx[k]
            if 0 <= y < 4 and 0 <= x < 4 and not visited[y][x]:
                visited[y][x] = True
                dfs(y, x, cur+board[y][x])
                visited[y][x] = False

    dx, dy = [0, 0, -1, 1, -1, -1, 1, 1], [-1, 1, 0, 0, -1, 1, -1, 1]
    W = int(input()) # 사전에 들어있는 단어의 수
    word_dict = {}
    for _ in range(W):
        word_dict[input().rstrip()] = 0
    input()

    B = int(input()) # 보드의 개수
    for _ in range(B):
        for k in word_dict.keys():
            word_dict[k] = 0

        board = [list(input().strip()) for _ in range(4)]
        input()

        for i in range(4):
            for j in range(4):
                visited = [[False]*4 for _ in range(4)]
                visited[i][j] = True
                dfs(i, j, board[i][j])
        score = 0
        longest = 0
        cnt = 0
        words = []
        chart = [0,0,0,1,1,2,3,5,11]

        for k, v in word_dict.items():
            if v > 0:
                if len(k) > longest:
                    longest = len(k)
                    words = [k]
                elif len(k) == longest:
                    words.append(k)
            
            score += chart[len(k)] * v
            cnt += v
        words.sort()
        print(score, words[0], cnt)

solution()