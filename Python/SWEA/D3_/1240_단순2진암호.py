import sys
sys.stdin = open('1240_단순2진암호.txt')
input = sys.stdin.readline
number = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
    }

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    line = 0
    flag = True
    graph = []
    result = []
    for i in range(n):
        graph.append(input().strip())
    for nums in graph:
        if not flag:
            break
        if int(nums) != 0:
            temp = []
            s = nums[::-1]
            for j in range(m):
                if s[j] == '1':
                    for k in range(j,j+56,7):
                        temp.append(s[k:k+7])
                    flag = False
                    break
            for i in range(8):
                result.append(number[temp[i][::-1]])
    
    result = result[::-1]
    s_odd = 0
    s_even = 0
    for i in range(0,8,2):
        s_odd += result[i]
    for i in range(1,8,2):
        s_even += result[i]
    if ((s_odd*3)+s_even)%10 == 0:
        print(f'#{test_case} {s_odd+s_even}')
    else:
        print(f'#{test_case} 0')