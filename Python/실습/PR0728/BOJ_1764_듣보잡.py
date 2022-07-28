from xml.dom import NOT_SUPPORTED_ERR


import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
no_seehear = {}
for i in range(N):                                           # 입력값 중 N개는 본적없는 사람
    a = input()
    no_seehear[a] = no_seehear.get(a, 0) + 1                 # 딕셔너리에 키 - 값 디폴트 0 , 본적없는 사람 == 1 
for i in range(M):                                           # N개 이후 M개는 들어본적 없는 사람
    a = input()                                             
    no_seehear[a] = no_seehear.get(a, 0) + 1                 # 딕셔너리에 키 - 값 디폴트 0, 본적없는사람인데 들어본적 없는사람 == 2

lst = sorted([k for k, v in no_seehear.items() if v == 2])   # 값이 2 인 키들을 리스트에 추가 후 정렬
print(len(lst))
for i in lst:
    print(i)