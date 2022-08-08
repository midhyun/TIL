from collections import Counter
lst = [1,1,1,1,2,3,4,5,6,6,6,6,6,1,5,5,5,5,5]
lst.sort()

cnt = Counter(lst).most_common(2)   # 가장 많이나온 숫자 2개를 (숫자, 개수) 튜플로 반환해줌.
print(cnt)
if len(cnt) > 1:                    # 2개가 나왔을때
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
