import sys
sys.stdin = open('17175_피보나치.txt')
input = sys.stdin.readline
result = 0
def fibonacci(n):
    global result
    result += 1
    result %= 1000000007
    if (n < 2):
        return n

    return fibonacci(n-2) + fibonacci(n-1)

fibonacci(int(input()))
print(result)  