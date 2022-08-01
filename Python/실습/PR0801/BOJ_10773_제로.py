T = int(input())
lst = []
for test_case in range(1, T+1):
    a = int(input())
    if a == 0:
        lst.pop()
    else:
        lst.append(a)
print(sum(lst))     