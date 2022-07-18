# 1) while
n = int(input())
a = 0
x = 0
while a != n:
    a += 1
    x += a
print(x)

# 2) for
n = int(input())
x = 0
for i in range(1,n+1) :
    x += i
print(x)