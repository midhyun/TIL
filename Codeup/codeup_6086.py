a = int(input())
b = 0
for i in range(1,a+1):
    b += i
    if b >= a :
        break
print(b)