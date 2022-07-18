N = int(input())
cnt = 0
for i in range(N):
    a = input()
    lst = []
    b = a[0]
    for j in range(len(a)):
        if j == len(a)-1 and a[j] in lst :
            break
        elif j == len(a)-1 and a[j] not in lst:
            cnt += 1
        else: pass
        if a[j] in lst:
            break
        elif a[j] not in lst:
            if a[j] == b:
                b = a[j]            
            else : 
                lst.append(b)
                b = a[j]
print(cnt)

