import sys
sys.stdin = open('14889_스타트와링크.txt')
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]
team = [N//2, N//2]
diff = 100
status = [0, 0]
s_lst = []
l_lst = []
def dps(depth, start, link):
    global diff
    if depth == N:
        diff = min(abs(status[0]-status[1]), diff)
        return
    
    if start:
        s_lst.append(depth)
        for i in s_lst:
            status[0] += stat[i][depth]
            status[0] += stat[depth][i]
        dps(depth +1, start -1, link)
        for i in s_lst:
            status[0] -= stat[i][depth]
            status[0] -= stat[depth][i]
        s_lst.pop()
    if link:
        l_lst.append(depth)
        for i in l_lst:
            status[1] += stat[i][depth]
            status[1] += stat[depth][i]
        dps(depth +1, start, link -1)
        for i in l_lst:
            status[1] -= stat[i][depth]
            status[1] -= stat[depth][i]
        l_lst.pop()

dps(0, team[0], team[1])
print(diff)