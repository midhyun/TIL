N = int(input())
# 4와 7로만 이루어진 수
num = N
while True:
    check = True
    for i in str(num):      # 각 자리의 수가 4 또는 7이 아니라면 
        if i not in '47':   # check = False
            check = False   # 한 자리라도 아닐 경우 다음 숫자로,
            break
    if check == True:       # check == True:
        print(num)          # 금민수 이므로 출력후 반복 종료
        break
    num -= 1                # num 에서 1씩 빼면서 검사, 가장 먼저 나온 값 = 가장 큰 값