import sys
sys.stdin = open('2469_사다리 타기.txt')
input = sys.stdin.readline
# A ~ Z : 65 ~ 90
K = int(input())
N = int(input())
final_pos = list(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(N)]

result = ['']*K
for i in range(K):
    result[i] = chr(i+65)

for i in range(N):
    if matrix[i][0] == '?':
        break
    for j in range(K-1):
        if matrix[i][j] == '-':
            result[j], result[j+1] = result[j+1], result[j]

for i in range(N-1, -1, -1):
    if matrix[i][0] == '?':
        break
    for j in range(K-1):
        if matrix[i][j] == '-':
            final_pos[j], final_pos[j+1] = final_pos[j+1], final_pos[j]



answer = ''
flag = True
for i in range(K-1):
    if not flag:
        answer += '*'
        flag = True
        continue

    if result[i] == final_pos[i]:
        answer += '*'
    else:
        final_pos[i], final_pos[i+1] = final_pos[i+1], final_pos[i]
        answer += '-'
        flag = False

if result == final_pos:
    print(answer)
else:
    print('x'*(K-1))