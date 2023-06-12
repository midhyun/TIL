list = [1,2,3,4,5]

def test(list1):
    list1 = list1[:]
    list1[1] = 'a'
    return list1

print(test(list))
print('---------------')
print(list)