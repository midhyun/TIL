# cnt = 0
# result = 0
# while 1000 > result:
#     cnt += 1
#     result += (cnt)
# print(cnt)

A, B = map(int, input().split()) # 입력
lst = []                         # 
for i in range(1,46):            # 1000개이상이 되는 범위
    for j in range(i):           # 리스트에서 A ~ B 범위의 숫자들을 리스트에 추가
        lst.append(i)

print(sum(lst[A-1:B]))           # 리스트에서인덱스 조정 후 합.