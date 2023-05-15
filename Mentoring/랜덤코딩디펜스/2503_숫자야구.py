import sys
sys.stdin = open('2503_숫자야구.txt')
input = sys.stdin.readline
permu_set = set()
check = [0]*10
def permu(cur, check):
    if len(cur) >= 3:
        permu_set.add(cur)
        return
    
    for i in range(1, 10):
        if not check[i]:
            tmp = cur + str(i)
            check[i] = 1
            permu(tmp, check)
            check[i] = 0
        
    
permu('', check)

N = int(input())
for i in range(N):
    q, strike, ball = map(int, input().split())
    q = str(q)
    tmp = set()
    for num in permu_set:
        strike_num, ball_num = 0, 0
        for k in range(3):
            if q[k] == num[k]:
                strike_num += 1
            elif num[k] in q:
                ball_num += 1
        if strike == strike_num and ball == ball_num:

            tmp.add(num)
    
    permu_set = tmp

print(len(permu_set))