# 알파벳 공부
# input : 알파벳 대,소문자로 이루어진 단어 길이는 100만 이하
# output : 가장 많이 사용된 알파벳 대문자로 출력// 여러개면 ? 출력

word = input().upper() # ABCDAAA
alpha = {}
for j in word: # A B C D A A A
    alpha[j] = alpha.get(j, 0) + 1
ma = max(alpha.values())
m_lst = []
for i in alpha:
    if alpha[i] ==  ma :
        m_lst.append(i)
if len(m_lst) == 1:
    print(m_lst[0])
else :
    print('?')