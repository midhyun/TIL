import sys
sys.stdin = open('1769_3의배수.txt')
input = sys.stdin.readline

X = input().strip()
cnt = []
def div_3(n):
    if len(n) == 1:
        print('YES')
        print(n,'---------------')
        return '이거 왜 안가져가?'
    else:
        S = 0
        for i in n:
            S += int(i)
        S = str(S)
        cnt.append(0)
        return div_3(S)

print(div_3(X))
print(len(cnt))
if int(X) % 3 == 0:
    print('YES')
else:
    print('NO')