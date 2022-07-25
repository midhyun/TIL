# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
for test_case in range(1, T+1):
    case = input().split('X')
    score = 0
    for i in case:
        if len(i) >= 1 :
            for j in range(1,len(i)+1):
                score += j
    print(score)
