import sys

sys.stdin = open("_민석이의과제체크하기.txt")
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T+1):             # test_case = T
    n ,k = map(int, input().split())        # n명의 총 학생, 과제를 제출한 k명의 학생
    report = set(map(int, input().split())) # 과제를 제출한 학생의 넘버 '세트'  //  제출 안한 학생을 탐색하기위해 복잡도가 적은 in set 사용하기 위함.
    lst = []                                # 과제를 안 제출한 학생의 넘버를 넣을 '빈 리스트'
    for i in range(1, n+1):
        if i not in report:                 # reprot'세트'에 n번째 학생의 넘버가 없다면, 과제 미제출
            lst.append(i)                   # 미제출 학생은 lst'리스트'에 담는다.
    print(f'#{test_case}',end =' ')
    print(*lst)