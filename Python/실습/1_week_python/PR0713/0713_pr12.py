# > 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

sts = 'apple'
sts = list(sts)
dl = 'a'
sts_dl = ''

while dl in sts :
    sts.remove(dl)
for i in sts:
    sts_dl += i
print(sts_dl)

# replace()
sts = 'apple'
print(sts.replace('a',''))