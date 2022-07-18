# S를 입력받은 후, 각문자를 R번 반복해 P를 출력하시오
T = int(input())
P = ''

for i in range(T):
    R, S = input().split()
    for j in S:
        print(j*int(R),end='')
    print()