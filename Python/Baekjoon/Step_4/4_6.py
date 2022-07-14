n = int(input())

for N in range(n):
    case = input().split('X')
    score = 0
    for i in case:
        if len(i) >= 1 :
            for j in range(1,len(i)+1):
                score += j
    print(score)