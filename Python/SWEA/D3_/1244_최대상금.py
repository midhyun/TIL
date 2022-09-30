import sys
sys.stdin = open('1244_최대상금.txt')


for tc in range(1,int(input())+1):
    data, k = input().split()                       # 숫자판의 정보, 교환횟수
    k = int(k)                                      # int(교환횟수)
    n = len(data)                                   # 숫자의 길이
    now = set([data])                               # 숫자의 종류
    nxt = set()
    for _ in range(k):
        while now:
            s = now.pop()                           # 숫자 set 에서 꺼냄
            s = list(s)                             # 리스트에 담아줌
            for i in range(n):                      # 숫자의 길이 0 ~ n
                for j in range(i+1,n):              # 현재 숫자의 위치 다음 부터 끝까지 i+1 ~ n , 중복 없는 순서쌍,
                    s[i],s[j] = s[j],s[i]           # 순서쌍 끼리 위치 바꾸고, 
                    nxt.add(''.join(s))             # nxt 라는 세트에 담아줌
                    s[i], s[j] = s[j], s[i]         # 원위치
        now,nxt = nxt,now                           # nxt에는 경우의 수가 중복없이 들어있고, now는 pop()을반복해서 비었다,
                                                    # 둘이 값을 바꾸고 이제 nxt가 빌때까지 now에 경우의 수를 담는다.

    print('#{} {}'.format(tc,max(map(int,now))))    # 모든 경우의 수 중에서 가장큰 값을 출력한다.