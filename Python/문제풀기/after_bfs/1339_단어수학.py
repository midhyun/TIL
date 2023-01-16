import sys
sys.stdin = open('1339_단어수학.txt')
input = sys.stdin.readline

n = int(input())
matrix = [[0]*8 for _ in range(n)]

for i in range(n):
    word = list(input().strip())
    for j in range(-1, -len(word)-1, -1):
        matrix[i][j] = word[j]

temp = {}
num = 9
for j in range(8):
    for i in range(n):
        if matrix[i][j] == 0: continue
        if matrix[i][j] in temp: temp[matrix[i][j]] += (10**(7-j))
        else:
            temp[matrix[i][j]] = (10**(7-j))
lst = []
for k, v in temp.items():
    lst.append((v, k))
lst.sort(reverse=True)
for alpha in lst:
    temp[alpha[1]] = num
    num -= 1

for j in range(8):
    for i in range(n):
        if matrix[i][j] == 0: continue
        matrix[i][j] = temp[matrix[i][j]]
result = 0
for mat in matrix:
    result += int(''.join([*map(str, mat)]))
print(result)
