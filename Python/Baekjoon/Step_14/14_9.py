import sys
sys.stdin = open('14_9.txt')
input = sys.stdin.readline

# 9375_패션왕 신해빈
# 의상의 이름과 종류, 
# 같은 종류는 한번에 한개만
# 경우의 수, 3종류일 경우  (a가지수)*(b가지수)*(c가지수) - 1(공집합 빼기, 하나라도 착용해야함)
# 2**n 인 이유는 선택 하거나 안하거나 2지선다인 경우
# type a = [hat,cap,0] hat이거나cap이거나 안쓰거나, 

T = int(input())
for test_case in range(1, T+1):
    n = int(input())                # 의상의 수
    types = {}
    for i in range(n):
        cloth, type = map(str, input().split()) 
        types[type] = types.get(type, 0) + 1
    result = 1
    for type, value in types.items():
        result *= value + 1 # 착용 안하는 경우를 추가해서 곱해줌
    print(result-1)
