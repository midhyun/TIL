import sys
sys.stdin = open('20546_기적의 매매법.txt')
input = sys.stdin.readline

cash = int(input())
jh_cash, jh_stock = cash, 0
sm_cash, sm_stock = cash, 0
tmp, up_cnt, down_cnt = None, 0, 0
price = [*map(int, input().split())]

for i in range(14):
    n = jh_cash // price[i]
    jh_cash -= n*price[i]
    jh_stock += n

    if tmp:
        if price[i-1] > price[i]:
            down_cnt += 1
            up_cnt = 0
        elif price[i-1] < price[i]:
            up_cnt += 1
            down_cnt = 0
    tmp = price[i]
    if up_cnt >= 3:
        sm_cash += sm_stock*price[i]
        sm_stock = 0
    elif down_cnt >= 3:
        n = sm_cash // price[i]
        sm_cash -= n*price[i]
        sm_stock += n

jh_cash += price[-1]*jh_stock
sm_cash += price[-1]*sm_stock
if jh_cash > sm_cash:
    print("BNP")
elif sm_cash > jh_cash:
    print("TIMING")
else:
    print("SAMESAME")