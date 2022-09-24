import sys
sys.stdin = open('1945_간단한소인수분해.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    dic = {2:0, 3:0, 5:0, 7:0, 11:0}
    for k in dic.keys():
        cnt = 0
        while True:
            if n%k == 0:
                n /= k
                cnt += 1
            else:
                break
        dic[k] += cnt
    print(f'#{test_case}', end=' ')
    print(*list(dic.values()))