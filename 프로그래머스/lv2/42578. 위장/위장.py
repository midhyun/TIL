def solution(clothes):
    dic_c = {}
    answer = 1
    for wear in clothes:
        dic_c[wear[1]] = dic_c.get(wear[1], 0) + 1

    for k, v in dic_c.items():
        answer *= (v+1)

    answer -= 1
    return answer