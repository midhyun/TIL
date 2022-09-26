import sys
sys.stdin = open('1206_View.txt')
input = sys.stdin.readline


for test_case in range(1, 11):
    n = int(input())
    lst = [*map(int, input().split())]
    dx = [-2,-1,1,2]
    result = 0
    for i in range(2,n-2):
        temp = []
        for k in range(4):
            x = i + dx[k]
            if lst[x] < lst[i]:
                temp.append(lst[i]-lst[x])
        if len(temp) == 4:
            result += min(temp)
    print(f'#{test_case} {result}')