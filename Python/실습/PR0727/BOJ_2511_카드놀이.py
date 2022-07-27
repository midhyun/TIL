import sys
sys.stdin = open('input.txt')

A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt_A = 0
cnt_B = 0
for i in range(len(A)):
    if A[i] > B[i]:
        cnt_A += 3
    elif A[i] < B[i]:
        cnt_B += 3
    elif A[i] == B[i]:
        cnt_A += 1
        cnt_B += 1

if cnt_A > cnt_B:
    print(cnt_A,cnt_B,sep=' ')
    print('A')
elif cnt_A < cnt_B:
    print(cnt_A,cnt_B,sep=' ')
    print('B')
else:
    for i in range(len(A)-1,-1,-1):
        if cnt_A == cnt_B:
            if A[i] > B[i]:
                print(cnt_A,cnt_B,sep=' ')
                print('A')
                break
            elif A[i] < B[i]:
                print(cnt_A,cnt_B,sep=' ')
                print('B')
                break
    else :
        print(cnt_A,cnt_B,sep=' ')
        print('D')
