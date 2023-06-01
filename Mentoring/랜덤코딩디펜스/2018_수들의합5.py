import sys
sys.stdin = open('2018_수들의합5.txt')
input = sys.stdin.readline

N = int(input())

def solution(N):
    s, e = 1, 1
    cnt = 0
    # s ~ e 까지 연속된 수를 더한 값이 
    # N보다 작으면 e +=1
    # N보다 크면 s +=1 
    while s < N+1:
        # 짝수면 홀수개
        if s == e:
            summary = s
        elif (e-s)%2 == 0:
            summary = (s+e)*((e-s+1)//2) + ((s+e)//2)
        else:
            summary = (s+e)*((e-s+1)//2)

        if summary > N:
            s += 1
        elif summary < N:
            e += 1
        else:
            cnt += 1
            e += 1

    print(cnt)
    
solution(N)