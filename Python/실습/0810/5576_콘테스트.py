import sys
sys.stdin = open('5576.txt')
input = sys.stdin.readline

# W, K 대학 10명씩 참가
# 높은 득점순 3명 =  대학 점수

W_scores = sorted([int(input()) for _ in range(10)],reverse=True)
K_scores = sorted([int(input()) for _ in range(10)],reverse=True)

print(sum(W_scores[:3]),sum(K_scores[:3]))