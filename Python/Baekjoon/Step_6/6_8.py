a = input() # D G J
b = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'.split()

result = 0
for i in a:
    for j in range(len(b)):
        if i in b[j]:
            result += j+3
print(result)