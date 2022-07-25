# A, B 를 입력받고 A+B를 출력
# T = test_case
# A,B ',' 로 구분
T = int(input())

for test_case in range(1,T+1):
    A, B = map(int,input().split(','))
    print(A+B)

# input의 위치를 생각해보자!!