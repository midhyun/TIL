import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    card_num = list(map(int, input().split()))  # 카드 번호 한개씩 리스트에 저장
    odd_even_sum = 0                            # 짝수번째 + 홀수번째

    for i in range(0,15):
        if (i+1) % 2 == 0:                      # 짝수번째 수는 그대로 더해주고,
            odd_even_sum += card_num[i]
        else:                                   # 홀수번째 수는 *2를 해서 더해준다.
            odd_even_sum += card_num[i]*2

    N = 10 - (odd_even_sum % 10)                # 마지막 N을 더해서 10으로 나누어 주었을때 나머지가 0
    if N == 10:                                 # N == 10 이면 0으로 변환.
        N = 0
    print(f'#{test_case} {N}')