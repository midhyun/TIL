def Rev(num):
    return num[::-1]

X, Y = input().split()
print(int(Rev(str(int(Rev(X)) + int(Rev(Y))))))