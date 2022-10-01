import sys
sys.stdin = open('1629_곱셈.txt')
input = sys.stdin.readline

def power(a, b, c, result):
    if b == 0:
        print(result)
        return
    ans = (result * a)
    power(a,b-1,c,result)




a, b, c = map(int, input().split())

power(a,b,c,1)