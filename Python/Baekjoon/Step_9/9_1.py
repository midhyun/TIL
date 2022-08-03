def factorial(num):                 # 팩토리얼 재귀함수
    if num <= 1:                    # num 이 1 이하일 경우 1 return
        return 1                    
    return num*factorial(num-1)     # num 이 1이 아닐경우 num * factorial(num-1)
print(factorial(10))                # num * num-1 * factorial(num-2)
                                    # num * num-1 * num-2 * factorial(num-3) if num == 1, return 1
                                    # 재귀에서도 종료 조건이 필요하다, while 반복처럼
