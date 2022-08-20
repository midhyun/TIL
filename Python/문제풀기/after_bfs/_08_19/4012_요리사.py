import sys
sys.stdin = open('4012_요리사.txt')
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input())

def dfs(depth, customer1, customer2):
    global diff
    if depth == N:
        diff = min(diff, abs(taste[0] - taste[1]))
        return
    
    if customer1:
        lst_ingd1.append(depth)
        for i in lst_ingd1:
            taste[0] += stats[i][depth]
            taste[0] += stats[depth][i]
        dfs(depth +1, customer1 -1, customer2)
        lst_ingd1.pop()
        for i in lst_ingd1:
            taste[0] -= stats[i][depth]
            taste[0] -= stats[depth][i]

    if customer2:
        lst_ingd2.append(depth)
        for i in lst_ingd2:
            taste[1] += stats[i][depth]
            taste[1] += stats[depth][i]
        dfs(depth +1, customer1 -1, customer2)
        lst_ingd2.pop()
        for i in lst_ingd2:
            taste[1] -= stats[i][depth]
            taste[1] -= stats[depth][i]
    



for test_case in range(1, T+1):
    N = int(input())
    stats = [list(map(int, input().split())) for _ in range(N)]
    taste = [0, 0]
    custom = [N//2, N//2]
    lst_ingd1 = []
    lst_ingd2 = []
    diff = 20000

    dfs(0, custom[0], custom[1])
    print(f'#{test_case} {diff}')