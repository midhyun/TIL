arr = [[1,1,1],[1,0,1],[1,1,1]]*3
for i in arr:
    for j in i:
        print(f"{'*'*j:>1}",end='')
    print()

