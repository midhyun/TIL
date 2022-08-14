import sys
sys.stdin = open('14_4.txt')
input = sys.stdin.readline
# 검문_2981
# 숫자 N 개를 종이에 적고, M 으로 나누었을때 나머지가 같게되는 M을 모두 찾기
# 시간초과
# 최대 공약수의 약수
N = int(input())
num_lst = [int(input()) for _ in range(N)]

def gcd(a, b):
    if b > a :
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

dif_num = []
for i in range(1, N):
    dif_num.append(abs(num_lst[i]-num_lst[i-1]))

gcd_ = dif_num[0]
for i in range(1, N-1):
    gcd_ = gcd(gcd_, dif_num[i])


result = [gcd_]
for i in range(2, int(gcd_**(1/2))+1):
    if gcd_ % i == 0:
        result.append(i)
        result.append(gcd_//i)
result = sorted(set(result))

print(*result)