from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

store_num = int(input())                                # 가게의 수
store_ = deque([*map(int, input().strip().split())])    # 가게마다 파는 우유의 종류 0==딸기,1==초코,2==바나나;
cnt_scb = 0                                             # 딸기 초코 바나나
cnt_milk = 0                                            # 마신 우유의 수
for i in range(store_num):                              # 가게마다 파는 우유 ?= 영학이가 마실 우유
    milk = store_[i]
    if milk == cnt_scb :
        cnt_scb += 1                                    # 딸 초 바 
        cnt_milk += 1                                   # 마신우유 +1
    if cnt_scb == 3:                                    # 바나나 다음엔 딸기
        cnt_scb = 0
print(cnt_milk)
    
