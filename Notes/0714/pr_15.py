word = 'banana'
cnt = 0
for i in word:
    if i == 'a':
        print(cnt)
        break
    cnt += 1
else :
    print(-1)

# 추가문제
word = 'HappyHacking'
cnt = 0
for i in word:
    if i == 'a':
        print(cnt, end=' ')
    cnt += 1