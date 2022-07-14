word = 'apple'
mo = ['a','e','i','o','u']
cnt = 0
for um in mo:
    for i in word:
        if i == um:
            cnt += 1
print(cnt)