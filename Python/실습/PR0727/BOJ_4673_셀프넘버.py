def karpka(num):
    for i in str(num):
        num += int(i)
    return num
karpka_lst = []
for i in range(1, 10001):
    karpka_lst.append(karpka(i))

for i in range(1,10001):
    if i not in karpka_lst:
        print(i)
