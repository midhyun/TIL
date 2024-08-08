import sys
sys.stdin = open('2836_수상택시.txt')
input = sys.stdin.readline

def solution(N, M, rev_people):
    result = 0
    rev_people.sort(reverse=True)
    start, end = 0, 0
    while rev_people:
        s, e = rev_people.pop()
        if start <= s <= end:
            end = max(e, end)
        elif end <= s:
            result += (end - start) * 2
            start, end = s, e
    result += (end - start) * 2
    print(result + M)

N, M = map(int, input().split())
rev_people = []
for _ in range(N):
    start, end = map(int, input().split())
    if end < start:
        rev_people.append((end, start))

solution(N, M, rev_people)