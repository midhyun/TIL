x = int(input())
y = 0
while x != 0 :
    x -= 1
    y += 1
    a ,b = map(int, input().split())
    print('Case #'+str(y)+': '+str(a)+' + '+str(b)+' = '+str(a+b))