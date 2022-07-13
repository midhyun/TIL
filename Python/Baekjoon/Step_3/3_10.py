n = int(input())
m = n
x = 0
while n != 0 :
    n -= 1 #4
    x += 1 #1
    stars = '*'*x
    print(f'{stars:>{m}}')