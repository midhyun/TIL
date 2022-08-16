import sys

sys.stdin = open("_반반.txt")

T = int(input())

for test_case in range(1, T+1):
    S = input()
    check = False
    if len(set(S)) == 2:
        for i in S:
            if S.count(i) == 2:
                check = True
    if check == True:
        print(f'#{test_case} Yes')
    else: print(f'#{test_case} No')