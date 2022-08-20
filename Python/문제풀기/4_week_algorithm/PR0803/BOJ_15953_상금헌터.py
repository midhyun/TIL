import sys
sys.stdin = open('15953.txt')
input = sys.stdin.readline
t = int(input())
a_prize, b_prize = (500,300,200,50,30,10), (512,256,128,64,32)
prize_rank_a, prize_rank_b = [0], [0]
for i in range(6):
    prize_rank_a += [a_prize[i] for _ in range(i+1)]
for i in range(5):
    prize_rank_b += [b_prize[i] for _ in range(2**i)]

for test_case in range(1, t+1):
    a_rank, b_rank = map(int, input().split())
    if a_rank >= len(prize_rank_a):
        a_rank = 0
    if b_rank >= len(prize_rank_b):
        b_rank = 0
    print((prize_rank_a[a_rank]+prize_rank_b[b_rank])*10000)

