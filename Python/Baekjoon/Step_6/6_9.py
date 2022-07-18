ca_lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
for i in ca_lst:
    a = a.replace(i,'a')
print(len(a))