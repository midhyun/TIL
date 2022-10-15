import sys
sys.stdin = open('5688_세제곱근.txt')
input = sys.stdin.readline

# t = int(input())
# for test_case in range(1, t+1):
#     n = int(input())
#     x = round(n**(1/3), 2)
#     if x**3 == n:
#         print(f'#{test_case}', int(x))
#     else:
#         print(f'#{test_case}', -1)

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    x = round(n**(1/3))
    if x**3 == n:
        print(f'#{test_case}', int(x))
    else:
        print(f'#{test_case}', -1)