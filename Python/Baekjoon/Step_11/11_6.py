num = input()
lst = sorted([int(i) for i in num],reverse=True)
result = ''
for i in lst:
    result += str(i)
print(result)

