A = input().split('=')
head = A.index('(^0^)')
print(A[:head].count('@'), A[head:].count('@'))
