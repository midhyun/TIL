import sys

sys.stdin = open("_괄호짝짓기.txt")
input = sys.stdin.readline
open_ = '([{<'
close_ = ')]}>'

for test_case in range(1, 11):
    check = True
    T = int(input())
    lines = input().strip()
    line_lst = []
    for i in lines:
        if i in open_:                                          # 여는괄호 일 때, 리스트에 추가
            line_lst.append(i)
        elif i in close_:                                       # 닫는 괄호 일때 리스트의 마지막 값과 쌍을 이루면, .pop()
            if close_.index(i) == open_.index(line_lst.pop()):  # 유효하지 않을 경우 check = False, break 반복문 종료
                continue
            else:
                check = False
                break
        
    if check == False:                                          # 괄호가 쌍을 이루지 않고 닫혔을 경우,
        print(f'#{test_case} 0')
    elif len(line_lst) != 0:                                    # 괄호가 열린채로 남아있어도 유효하지 않음,
        print(f'#{test_case} 0')
    else: print(f'#{test_case} 1')                              # 모든 괄호가 닫혔을 경우,