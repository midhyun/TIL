import sys
sys.stdin = open('16472_고냥이.txt')
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
s_dic = {}

s, e, result, tmp = 0, 0, 0, 0

while True:
    # 사용한 문자열의 개수가 N개 이하일경우, 추가할지 말지결정
    if len(s_dic) < N or (len(s_dic) == N and S[e] in s_dic):
        s_dic[S[e]] = s_dic.get(S[e], 0) + 1
        e += 1
        tmp += 1
        result = max(result, tmp)
    # 추가가 불가능할 경우 start를 +1 해줌.
    else:
        s_dic[S[s]] -= 1
        if s_dic[S[s]] == 0:
            s_dic.pop(S[s])
        s += 1
        tmp -= 1
    # 마지막문자 까지 삽입 했을 경우 반복문 종료.
    if e == len(S):
        break

print(result)    