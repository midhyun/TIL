import sys
sys.stdin = open('9613_GCD합.txt')
input = sys.stdin.readline

def find_GCD(a, b):
    while True:
        if b > a: a, b = b, a
        remain = a % b
        a, b = b, remain
        if b == 0:
            return a

# 유클리드 호제법
T = int(input())
for _ in range(T):
    integer = [*map(int, input().split())]
    result = 0
    for i in range(1, len(integer)):
        for j in range(i+1, len(integer)):
            result += find_GCD(integer[i], integer[j])
    
    print(result)