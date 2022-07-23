M = int(input())
i = 2
while M != 1:
    sosu = True
    if sosu == True and M % i == 0:
        M /= i
        print(i)
        continue
    else : i += 1

# 시간초과...
