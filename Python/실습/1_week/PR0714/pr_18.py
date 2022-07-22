word = 'banana'
st_word = set(in_word) 
out_word = {}
# 1
for i in st_word:      ## 중복값을 제거 할 순 있지만,  순서가 없어서 실행마다 결과값의 순서가 다름. 
    out_word[i] = 0
for i in word:
    out_word[i] += 1   
for k, v in out_word.items():
    print(k, v)
# 2
for i in word:
    if i in out_word:
        out_word[i] += 1
    else :
        out_word[i] = 1
for k in out_word:
    print(k, out_word[k])

# T
result = {}

for char in word:
    result[char] = result.get(char, 0) + 1
for k in result:
    print(k, result[k])
