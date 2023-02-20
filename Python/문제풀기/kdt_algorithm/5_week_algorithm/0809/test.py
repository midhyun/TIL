import sys
sys.stdin = open('1371.txt')
input = sys.stdin.read
lst = []
alpha_dict = {}


lst.append(input().strip().split('\n'))             # 2차원 리스트로 각 줄을 각 행으로 구분

for i in lst:                                       # 각 행리스트 안의 문장
    for j in i:                                     # 문장의 알파벳 순회
        alpha_dict[j] = alpha_dict.get(j, 0) + 1    # 리스트에 담아주고 개수를 세어줌

alpha_dict[' '] = 0                                 # 공백도 담겼으므로 0으로 바꿔줌
p_lst = []

for k, v in alpha_dict.items():                     # 딕셔너리에서 가장 큰 값을 가진 키를 p_lst에 담아줌
    if v == max(alpha_dict.values()):
        p_lst.append(k)

p_lst.sort()                                        # 오름차순으로 정렬

for _ in p_lst:                                     # 리스트에 담긴 알파벳을 오름차순으로 출력
    print(_,end='')