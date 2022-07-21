X = int(input())
cnt = 0
arr = 1
while arr <= X:
    arr += cnt
    cnt += 1
n = X - (arr - cnt)
if cnt % 2 == 0 :
    print(f'{(cnt-n)}/{n}')
else : print(f'{n}/{(cnt-n)}')