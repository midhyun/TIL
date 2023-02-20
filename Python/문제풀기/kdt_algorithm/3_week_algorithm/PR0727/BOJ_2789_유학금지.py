import sys
sys.stdin = open('input.txt')

censorship = 'CAMBRIDGE'
result = input()
for i in censorship:
    result = result.replace(i,'')
print(result)