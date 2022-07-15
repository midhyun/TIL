numbers = [0, 20, 100, 50, -60, 50, 100]
numbers = list(set(numbers))
a = numbers[0]

for i in numbers :
    if a <= i :
        a = i
print(a)