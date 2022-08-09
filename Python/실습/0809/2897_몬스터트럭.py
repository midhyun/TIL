import sys
sys.stdin = open('2897.txt')
input = sys.stdin.readline
# 1. 안 부수면서 주차할수 있는 공간의 개수
# 2. 한 대를 부수고 주차할 수 있는 공간의 개수
# 3. 두 대를 부수고 주차할 수 있는 공간의 개수
# 4. 세 대를 부수고 주차할 수 있는 공간의 개수
# 5. 네 대를 부수고 주차할 수 있는 공간의 개수
destroy_dic = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0}           # 0~ 4대를 부수고 주차할 수 있는 공간의 개수 딕셔너리
R, C = map(int, input().split())
matrix = [[i for i in input().strip()] for _ in range(R)]
dx = [0,1,0,1]                                              # 델타 탐색
dy = [0,0,1,1]

for i in range(R-1):                                        # 델타의 범위에 따라 마지막 한칸전 까지 순회
    for j in range(C-1):
        cnt = 0                                             # 부수는 차의 개수
        check = True                                        # 주차 가능 여부
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < C and 0 <= y < R:                   # matrix 범위 내에서 델타 탐색
                if matrix[y][x] == 'X':                     # 탐색 범위안에 'X'가 있을경우, 부수는 차 +1
                    cnt += 1
                elif matrix[y][x] == '#':                   # 탐색 범위 안에 '#'이 있을 경우, 주차 불가
                    check = False
                    break
        if check == False:                                  # 주차 불가일 경우 pass 다음 반복으로 넘어감.
            pass
        else:                                               # cnt(부수는 차의 개수) 공간의 개수 + 1
            destroy_dic[cnt] += 1
        
for i in range(5):                                          # 딕셔너리에 담긴 값들을 출력함.
    print(destroy_dic[i])