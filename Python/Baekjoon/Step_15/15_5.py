import sys
from pprint import pprint
sys.stdin = open('15_5.txt')
input = sys.stdin.readline
# N-Queen_9663
# N x N 체스판위에 퀸 N개를 서로 공격할 수없게 놓는 문제
# 퀸을 놓는 방법의 수를 구하시오.

# N*N 보드에 퀸 N개 놓으려면 한 행에 하나씩,, 들어가야되네
N = int(input())

board = [0]*N
print(board)
