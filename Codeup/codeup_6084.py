h, b, c, s = map(int,input().split())
ss = (h*b*c*s)/8/1024/1024
print('{:.1f} MB'.format(ss))

print(f'{ss:.1f} MB',sep=' ')