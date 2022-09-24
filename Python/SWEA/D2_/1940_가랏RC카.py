import sys
sys.stdin = open('1940_가랏RC카.txt')
input = sys.stdin.readline 

# 현재 속도
# 가속인지 감속인지
# 현재속도 = 0 
# 가속 OR 감속 + -
# 가속도 
# 현재속도 
# 이동거리 = 속도 x 시간(1s) << 시간이 1초마다 커맨드
#  1 2 처음 1초
#  2 1 다음 1초
# + 2 - 1 거리가 아니라 속도 
# 거리>> 2+1 만큼 이동한거죠 
# 3 거/속 x 시

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    pos = 0
    v = 0
    for i in range(n):
        x = input().strip() # '1 1 t'/ '0'
        if len(x) == 1:
            pos += v
        else:
            status, acc = map(int, x.split())
            if status == 1:
                v += acc
            elif status == 2:
                v = max(v-acc, 0)
            pos += v
    print(f'{test_case} {pos}')