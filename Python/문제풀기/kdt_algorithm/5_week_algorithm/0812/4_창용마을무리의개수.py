import sys

sys.stdin = open("_창용마을무리의개수.txt")
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N 사람 수, M 관계 수
    in_lst = [[] for _ in range(N+1)]         # 빈 인접리스트
    check = [False]*(N+1)                   # 체크리스트 * 사람 수
    for i in range(M):                      # 인접 리스트 채우기
        i, j = map(int, input().split())
        in_lst[i].append(j)
        in_lst[j].append(i)
    cnt = 0
    for i in range(1, N+1):
        if not check[i]:
            cnt += 1
            stack = [i]
            check[i] = True
            while stack:
                person = stack.pop()
                for j in in_lst[person]:
                    if not check[j]:
                        check[j] = True
                        stack.append(j)
    print(f'#{test_case} {cnt}')