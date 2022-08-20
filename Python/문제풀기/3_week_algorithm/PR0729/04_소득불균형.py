import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    people = int(input())
    lst_earn = list(map(int, input().split()))
    avg_earn = float(sum(lst_earn)/people)

    result_cnt = 0
    for earn in lst_earn:
        if earn <= avg_earn:
            result_cnt += 1
    print(f'#{test_case} {result_cnt}')