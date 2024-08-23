import sys
sys.stdin = open('1850_최대공약수.txt')
input = sys.stdin.readline

# 유클리드 호제법(알고리즘)
# 2개의 자연수 또는 정식의 최대공약수를 구하는알고리즘의 하나이다.
# 두 수가 서로 상대방 수를 나누어 결국 원하는 수를 얻는 알고리즘.
# 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(a>b일 때)
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 이를 반복해서
# 나머지가 0이 될 때 나누는 수가 a와 b의 최대공약수 이다.
def solution(a, b):
    if a < b:
        a, b = b, a

    while a % b:
        a, b = b, a % b
    return b

N, M = map(int, input().split())
print('1' * solution(N, M))