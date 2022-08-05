import sys

sys.stdin = open("_파리퇴치.txt")
input = sys.stdin.readline
T = int(input())

for test_case in range(1, T+1):
    catch_lst = []
    N, M = map(int, input().split())                                # N x N 배열, 'M x M 크기의 파리채'
    matrix = [list(map(int, input().split())) for _ in range(N)]    # 배열 생성
    dx = list(range(M))*M                                           # 파리채 x 범위
    dy = [i for i in range(M) for _ in range(M)]                    # 파리채 y 범위
    for i in range(N):                                              # 모든 배열 인덱스 순회
        for j in range(N):
            catch = 0                                               # catch 값 0으로 초기화
            for k in range(M*M):                                    # 각 인덱스위치에서 파리채 범위의 값들을 catch에 더해줌
                y = i+dy[k]
                x = j+dx[k]
                if 0 <= x <= N-1 and 0 <= y <= N-1:                 # out of range가 발생하지 않도록 범위 조건 부여
                    catch += matrix[y][x]
            catch_lst.append(catch)                                 # 파리채가 잡은 catch값 '리스트'에 추가
    print(f'#{test_case} {max(catch_lst)}')                         # '리스트'의 max() 값을 출력
            