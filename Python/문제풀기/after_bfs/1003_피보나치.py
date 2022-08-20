import sys
sys.stdin = open('1003_피보나치.txt')
input = sys.stdin.readline

T = int(input())

def fibo(n):
    if n == 0:
        cnt_0.append(1)
        return dic[0]
    elif n == 1:
        cnt_1.append(1)
        return dic[1]

    if n in dic:
        return dic[n]

    dic[n] = fibo(n-1) + fibo(n-2)
    return dic[n]

dic = {0:0, 1:1}
for test_case in range(1, T+1):
    N = int(input())
    cnt_0 = []
    cnt_1 = []
    if N == 0:
        print(1, 0)
    else:
        print(fibo(N-1),fibo(N))