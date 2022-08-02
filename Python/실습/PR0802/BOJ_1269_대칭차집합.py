import sys
sys.stdin = open('1269.txt')
input = sys.stdin.readline

A, B = map(int, input().split())

A_set = set([*map(int, input().split())])               # set 끼리 차집합 연산
B_set = set([*map(int, input().split())])

# print(len((A_set | B_set) - (B_set & A_set)))   # 합집합 - 교집합 // 집합 합 연산은 + 가 아닌 | 사용
print(len(A_set^B_set))                           # 대칭 차 = 합집합 - 교집합