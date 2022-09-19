import sys
sys.stdin = open('D2_2005.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    print(f'#{test_case}')
    result_b = [1]
    result_cur = [1]
    for i in range(1, n+1):
        if i == 1:
            print(1)
            continue
        for j in range(1,i-1):
            result_cur.append(result_b[j-1]+result_b[j])
        result_cur.append(1)
        for i in result_cur:
            print(i, end=' ')
        print()
        result_b = result_cur
        result_cur = [1]