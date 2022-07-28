import sys
sys.stdin = open('input.txt')

n = int(input())
giggle_dict = {}
lst = []
for i in range(n):                  # n번 순회
    A, B = map(str,input().split()) 
    giggle_dict[A] = B              # giggle_dict에 key(이름) : value('enter' or 'leave') 추가

for i in giggle_dict:               # 딕셔너리의 값이 'enter' 인 경우 리스트에 이름 추가
    if giggle_dict[i] == 'enter':
        lst.append(i)

lst.sort(reverse = True )           # 내림차순 정렬
for i in lst:                       # 회사에 'enter' 하고 'leave' 하지 않은 key(이름) 출력
    print(i)