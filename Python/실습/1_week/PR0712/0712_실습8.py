numbers = [0, 1, 0]
a = numbers[0]
for i in numbers :
    if a <= i :
        a = i
else :
    while a in numbers :
        numbers.remove(a)
b = numbers[0]
for i in numbers :
    if b <= i :
        b = i
print(b)