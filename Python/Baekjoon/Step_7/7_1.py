A, B, C = map(int,input().split())
try:
    if A/(C-B) > 0:
        print(int(A//(C-B))+1)
    else :
        print(-1)
except:
    print(-1)
