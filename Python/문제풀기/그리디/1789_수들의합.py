import sys
sys.stdin = open('1789_수들의합.txt')
input = sys.stdin.readline

now = 1
temp = 0
num = int(input())
while True:
    temp += now
    if temp > num:
        break
    
    now += 1
print(now -1)