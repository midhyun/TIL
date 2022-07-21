# input N : 배달해야하는 설탕 무게
# 설탕은 3kg, 5kg 단위
# 안나눠지면 -1

N = int(input())
if  N > 5 and N % 5 == 1:
    print((N//5)+1)
elif N > 5 and N % 5 == 4:
    print((N//5)+2)
elif N > 10 and N % 5 == 2:
    print((N//5)+2)
elif (N % 5) % 3 == 0:
    print((N//5) + (N%5)//3)
else :
    print(-1)