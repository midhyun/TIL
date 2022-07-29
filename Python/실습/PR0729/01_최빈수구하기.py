import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):

    case_num = int(input())
    scores = list(map(int, input().split()))
    score_dict = {}
    

    for i in scores:
        score_dict[i] = score_dict.get(i, 0) + 1

    mod = sorted([k for k, v in score_dict.items() if max(score_dict.values()) == v],reverse = True)
    print(f'#{case_num} {mod[0]}')
