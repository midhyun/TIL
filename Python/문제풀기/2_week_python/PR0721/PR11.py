# 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.

# (시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    h_1, m_1, h_2, m_2 = map(int,input().split())
    re_m = (m_1 + m_2) % 60
    re_h = ( h_1 + h_2 + (m_1 + m_2)//60 ) % 12
    if re_h == 0 :
        re_h = 12
    print(f'#{test_case} {re_h} {re_m}')