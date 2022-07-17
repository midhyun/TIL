# 알파벳 찾기
# input : 단어 S // 단어의 길이는 100이하 알파벳 소문자
# output : 각 알파벳의 첫 등장 위치 , 없다면 -1 ,첫글자는 0번

a = input()
for i in range(97,123):
    num = 0
    for j in a:
        if chr(i) != j:
            num += 1
        elif chr(i) == j:
            break
    if num == len(a):
        print('-1',end=' ')
    else:
        print(num,end=' ')