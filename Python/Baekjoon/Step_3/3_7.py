a = int(input())
x = 0
while a != 0 :
    a -= 1
    x += 1
    b ,c = map(int, input().split())
    print('Case #'+str(x)+': '+str(b + c))