# Fn = Fn-1 + Fn-2 (n ≥ 2)

def fibo(num):
    if num == 1 :                       # num == 1 이면 1
        return 1
    elif num == 0 :                     # num == 0 이면 0
        return 0
    return fibo(num-1) + fibo(num-2)    # num-1 + num-2 
n = int(input())
print(fibo(n))

                                        # f(n) = f(n-1) + f(n-2) 이므로 f(n-1) = f(n-2) + f(n-3) 이다. 
                                        # .... f(1) + f(0) == 1 이므로 f(2) == f(1) + f(0) == 1, f(3) == f(2) + f(1) 로 다시 재귀함.
                                        # 즉 f() 함수의 리턴에 재귀함수 개수만큼 재귀가 종료되는 조건이 필요함.