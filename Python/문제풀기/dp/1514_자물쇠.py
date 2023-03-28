import sys
sys.stdin = open('1514_자물쇠.txt')
input = sys.stdin.readline

N = int(input())  # 디스크의 개수

cur = list(map(int, input().strip()))  # 현재 자물쇠의 상태
pwd = list(map(int, input().strip()))  # 세준이의 비밀번호

min_rot = [0] * N  # 각 디스크에서의 최소 회전 횟수를 저장할 리스트
total_rot = 0  # 최종 회전 횟수를 저장할 변수

for i in range(N):
    # 각 디스크에서의 최소 회전 횟수 계산
    diff = abs(cur[i] - pwd[i])
    min_rot[i] = min(diff, 10 - diff)
    
    # 최소 회전 횟수를 계산하는 것은 세 개의 디스크를 동시에 회전하는 것이 가능
    # 최대 세 개의 디스크를 묶어서 최소 회전 횟수를 계산
    if i >= 2:
        total_rot += min_rot[i-2:i+1]

# 최종 회전 횟수 출력
print(min(total_rot))