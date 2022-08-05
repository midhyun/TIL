import sys
sys.stdin = open('2776.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    seen = int(input())                         # 본 숫자 개수
    lst_seen = set(map(int, input().split()))   # 세트 // 중복값이 없을 경우 세트를 사용하는 것이 반복문에서 유리하다.
    Q = int(input())                            # 물어볼 숫자 개수
    lst_Q = list(map(int, input().split()))     # 물어볼 숫자 리스트 // 세트는 순서가 보장되지 않기 때문에 리스트로 사용했다.
    
    for num in lst_Q:
        if num in lst_seen:                     # 세트에 in 연산은 평균 O(1)이다.
            print(1)
        else: print(0)