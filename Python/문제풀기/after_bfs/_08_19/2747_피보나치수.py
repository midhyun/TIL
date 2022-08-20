import sys
sys.stdin = open('2747_피보나치수.txt')

n = int(input())
dic = {0:0, 1:1}
def fibonacci(num):
    if num in dic:
        return dic[num]
    dic[num] = fibonacci(num-1) + fibonacci(num-2)
    return dic[num]

print(fibonacci(n))