N, X = map(int, input().split())

A = list(map(int, input().split()))

for s_num in A:
    if s_num < X :
        print(s_num, end=' ')
