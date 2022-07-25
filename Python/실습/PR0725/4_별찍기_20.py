N = int(input())
for i in range(1, N+1):
    stars = '* '*N
    if i % 2 == 0:
        print(' ' + stars)
    else: print(stars)
