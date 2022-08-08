import sys
sys.stdin = open('1543.txt')
input = sys.stdin.readline

docs_ = input().strip()
search_word = input().strip()
result = docs_.replace(search_word, '0')
print(result.count('0'))