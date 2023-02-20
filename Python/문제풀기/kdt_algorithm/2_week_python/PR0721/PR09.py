# N, 2N, ... kN = dict
# for i in range N:
T = int(input())
for test_case in range(1, T+1):
    lst = []
    N = int(input())
    M = 0
    while len(set(lst)) != 10 :
        M += N
        for i in str(M):
            lst.append(i)
    print(f'#{test_case} {M}')