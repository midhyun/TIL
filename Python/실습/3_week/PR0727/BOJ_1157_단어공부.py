# 가장 많이 사용된 알파벳 
word = list(input().upper())  # 입력받은 단어를 대문자로 변환후 리스트에 담아줌. aaaaaabbbbbbcdfeedee [ a,a,c,a,a,a,a,a,b,b,b,b,c,d,f,ee]
word_set = list(set(word)) # 중복값을 제거 [a,b,c,d,e,f]
cnt_lst = [10,5,4,3,2] # 알파벳 갯수 리스트 = 10 개 어떤게 10인지<<
result = ''

for spell in word_set: # 단어의 갯수를 리스트에,
    num_spell = word.count(spell)
    cnt_lst.append(num_spell) 

cnt_m = max(cnt_lst) # 리스트에서 가장큰 값 == 가장 많이 사용된 문자의 갯수 a= 10, b=10 // 

for spell in word_set:  # 가장 많이 사용된 문자의 갯수와 일치하는 문자를 결과에 넣음.
    if word.count(spell) == cnt_m:
        result = spell

if cnt_lst.count(cnt_m) == 1: # 가장 많이사용된 알파벳이 한개일경우 프린트, 여러개일경우 물음표
    print(result)
else:
    print('?')