import sys
sys.stdin = open('D2_1983.txt')
input = sys.stdin.readline

t = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    lst = []
    for i in range(1, n+1):
        mid, final, report = map(int, input().split())
        score = (mid*0.35) + (final*0.45) + (report*0.2)
        lst.append((i,score))
    lst.sort(key=lambda x: -x[1])
    result = ''
    for i in range(len(lst)):
        if lst[i][0] == k:
            result = grade[i//(n//10)]
            break
    print(f'#{test_case} {result}')