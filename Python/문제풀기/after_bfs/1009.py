import sys
sys.stdin = open('1009.txt')
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    a, b = map(int, input().split())
    a %= 10
    result = 1
    lst = []
    if a == 0:
        print(10)
    else:
        for _ in range(b):
            result *= a
            result %= 10
            if result in lst:
                print(lst[(b-1)%len(lst)])
                break
            lst.append(result)
        else:
            print(result)