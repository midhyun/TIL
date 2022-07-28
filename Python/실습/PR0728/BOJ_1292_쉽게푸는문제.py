# cnt = 0
# result = 0
# while 1000 > result:
#     cnt += 1
#     result += (cnt)
# print(cnt)

A, B = map(int, input().split())
lst = []
for i in range(1,46):
    for j in range(i):
        lst.append(i)

print(sum(lst[A-1:B]))