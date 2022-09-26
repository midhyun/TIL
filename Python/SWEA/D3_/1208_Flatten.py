import sys
sys.stdin = open('1208_Flatten.txt')
input = sys.stdin.readline



for test_case in range(1, 11):
    dump = int(input())
    lst = [*map(int, input().split())]
    for i in range(dump):
        lst.sort()
        if lst[-1] - lst[0] > 1:
            lst[0] += 1
            lst[-1] -= 1
        else:
            break
    lst.sort()
    print(f'#{test_case} {lst[-1]-lst[0]}')