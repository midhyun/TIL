# > 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

word = 'apple'
rw = ''
n = len(word)
num = 0
for i in range(n-1,-1,-1):
    rw += word[i]
    num += 1
print(rw)

# 슬라이싱

print(word[::-1])