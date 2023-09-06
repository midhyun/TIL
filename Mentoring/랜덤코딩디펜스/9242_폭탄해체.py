import sys
sys.stdin = open('9242_폭탄해체.txt')
input = sys.stdin.readline

bomb = [input().rstrip() for _ in range(5)]
N = (( len(bomb[0]) ) // 4) + 1
zero = ['***','* *','* *','* *','***']
one = ['  *','  *','  *','  *','  *']
two = ['***','  *','***','*  ','***']
three = ['***','  *','***','  *','***']
four  = ['* *','* *','***','  *','  *']
five = ['***','*  ','***','  *','***']
six = ['***','*  ','***','* *','***']
seven = ['***','  *','  *','  *','  *']
eight = ['***','* *','***','* *','***']
nine = ['***','* *','***','  *','***']
nums = [zero,one,two,three,four,five,six,seven,eight,nine]
check = [False]*5
check_all = [False]*10
ans_list = []

for i in range(N):
    for n in range(10):
        for j in range(5):
            if bomb[j][4*i:4*i+3] == nums[n][j]:
                check[j] = True
        if all(check):
            check_all[n] = True
            ans_list.append(n)
        check = [False]*5
    if any(check_all):
        check_all = [False]*10
        continue
    else:
        print("BOOM!!")
        exit()

ans = 0
for i in range(1, N+1):
    ans += ans_list[-i] * (10**(i-1))
if ans%6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")