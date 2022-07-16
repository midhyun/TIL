N = int(input())
lst_han = []
for n in range(1,N+1):
    nb = 0
    sn = str(n)    
    if n < 100:
        lst_han.append(n)
    else:
        for j in range(1,len(sn)):
            AP = int(sn[0])-int(sn[1])
            sm = int(sn[j-1])-int(sn[j])
            if AP == sm :
                nb += 0
            else:
                nb += 1
        if nb == 0:
            lst_han.append(n)
print(len(lst_han))

