import sys
sys.stdin = open('prg_성격유형검사.txt')
input = sys.stdin.readline

n = int(input())                        # 점수가 같을 경우 사전순

for test_case in range(1, n+1):
    ans = ''
    case_ = {'R': 0,'T': 0,'C': 0,'F': 0,'J': 0,'M': 0,'A': 0,'N': 0}
    survey = input().strip().split()
    choices = [*map(int, input().split())]
    scores = [0,3,2,1,0,1,2,3]

    for i in range(len(survey)):
        score = scores[choices[i]]
        if choices[i] < 4:
            case_[survey[i][0]] += scores[choices[i]]
        else:
            case_[survey[i][1]] += scores[choices[i]]

    case_lst = list(case_)
    for i in range(0,8,2):
        if case_[case_lst[i]] >= case_[case_lst[i+1]]:
            ans += case_lst[i]
        else : ans += case_lst[i+1]

    print(ans)