import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
s_dic = {}

s, e, result, tmp = 0, 0, 0, 0

while True:
    
    if len(s_dic) < N or (len(s_dic) == N and S[e] in s_dic):
        s_dic[S[e]] = s_dic.get(S[e], 0) + 1
        e += 1
        tmp += 1
        result = max(result, tmp)
    else:
        s_dic[S[s]] -= 1
        if s_dic[S[s]] == 0:
            s_dic.pop(S[s])
        s += 1
        tmp -= 1

    if e == len(S):
        break
print(result)    
