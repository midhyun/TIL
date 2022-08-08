import sys
from collections import Counter
sys.stdin = open('11_5.txt')
input = sys.stdin.readline

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙 값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()
print(round(sum(lst)/len(lst))) # 산술평균 소수점 첫째자리 반올림
print(lst[len(lst)//2]) # 중앙값
cnt = Counter(lst).most_common(2)

if len(lst) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(lst) - min(lst))