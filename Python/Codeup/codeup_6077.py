a = int(input())
b = 0

for i in range(1, a+1):
    if i % 2 == 0 :
        b += i
print(b)