# 1) While
word ='happy'
wl = list(word)
long = 0

while wl :
    wl.pop(0)
    long += 1

print(long)

# 2) For
words = 'happy'
long = 0
for word in words :
    long += int(bool(word))

print(long)


# 3) For - idx
word = 'happy'
long = 0
for i in word :
    long += 1
print(long)
