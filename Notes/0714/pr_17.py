word = 'apple'
up = ''
for i in word:
    up += chr(ord(i)-32)
print(up)

# 추가하는 방식을 다르게

for i in word:
    print(chr(ord(i)-32),end='')