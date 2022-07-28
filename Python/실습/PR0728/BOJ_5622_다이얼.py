dial = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'.split() # 각 번호에 해당하는 문자들끼리 묶어서 리스트로 만들어줌.
call_num = input()                                 # 할머니의 문자를 입력받음
result = 0                                         # 걸리는 시간 결과.
for i in call_num:                                 # 할머니의 문자를 하나씩 순회함
    for j in range(len(dial)):                     # 리스트의 인덱스 넘버 0 ~ 8 을 range로 순회함
        if i in dial[j]:                           # 리스트를 순회하면서 리스트 안의 문자열도 순회함
            result += j+3                          # 할머니 문자 == 리스트 문자 >> 해당 인덱스 넘버 + 3 만큼의 시간 추가
    
print(result)                                      # 시간 출력. ABC 2번  1번 2초// 2번 3초 list[0] << 0 + 3 , 3번 4초가 4초//

