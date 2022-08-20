import sys
sys.stdin = open('1769_3의배수.txt')
input = sys.stdin.readline

X = input().strip()
cnt = []
def div_3(n):
    if len(n) == 1:
        return n
    S = 0
    for i in n:
        S += int(i)
    S = str(S)
    cnt.append(0)
    return div_3(S)

a = int(div_3(X))
print(len(cnt))
if a % 3 == 0:
    print('YES')
else:
    print('NO')