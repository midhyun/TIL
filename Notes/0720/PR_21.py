a = int(input())
cnt = 0
lst = []
b = 0
while a:    
    lst.append(a % 10)
    a = a//(10)
    cnt += 1
lst.reverse()
for i in range(cnt-1,-1,-1):
    b += lst[i]*(10**i)
print(b)