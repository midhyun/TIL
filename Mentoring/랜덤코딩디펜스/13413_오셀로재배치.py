import sys
sys.stdin = open('13413_오셀로재배치.txt')
input = sys.stdin.readline

def solution():
    T = int(input())
    for test_case in range(T):
        N = int(input())
        init = input().rstrip()
        goal = input().rstrip()
        diff_cnt = 0
        result = 0
        cnt_white, goal_white = init.count('W'), goal.count('W')
        for i in range(N):
            if init[i] != goal[i]:
                diff_cnt += 1
        result += abs(cnt_white - goal_white)
        diff_cnt -= abs(cnt_white - goal_white)
        if diff_cnt % 2 == 1:
            result += 1
            diff_cnt -= 1
        
        diff_cnt //= 2
        result += diff_cnt
        print(result)
                

solution()