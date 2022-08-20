import sys
sys.stdin = open('input.txt')
lst = []
result = []
for i in range(5):
    lst.append(f'{input():<15}')

for i in range(15):
    for j in range(5):
        result.append(lst[j][i])

print(''.join(result).replace(' ',''))