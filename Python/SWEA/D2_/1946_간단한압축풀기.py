import sys
sys.stdin = open('1946_간단한압축풀기.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    alphabets = ''
    lst = []
    for i in range(n):
        alphabet, num = input().strip().split()
        num = int(num)
        alphabets += (alphabet*num)
    temp = len(alphabets)//10
    temp_ = len(alphabets)%10
    for i in range(temp):
        lst.append(alphabets[0+(10*i) : 10+(10*i)])
    lst.append(alphabets[10+(10*i):])
    print(f'#{test_case}')
    for i in lst:
        print(i)