import sys
sys.stdin = open('2631_줄세우기.txt')
input = sys.stdin.readline

# N명의 아이들
N = int(input())
pos_child = []
for _ in range(N):
    pos_child.append(int(input()))

