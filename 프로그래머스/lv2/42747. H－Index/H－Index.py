def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(1, len(citations)+1):
        if citations[i-1] >= i:
            answer = i

    return answer