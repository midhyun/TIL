w, h ,b = map(int,input().split())
ss = (w*h*b)/8/1024/1024
print('{:.2f} MB'.format(ss))