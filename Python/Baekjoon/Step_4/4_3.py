A = int(input())
B = int(input())
C = int(input())
D = list(str(A*B*C))
for num in range(10):
    cnt_arg = 0
    for i in D:
        if num == int(i):
            cnt_arg += 1
    print(cnt_arg)