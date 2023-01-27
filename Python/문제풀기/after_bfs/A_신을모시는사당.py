import sys
sys.stdin = open('A_신을모시는사당.txt')
input = sys.stdin.readline

n = int(input())
stones = [*map(int, input().split())]

left = 0
right = 0
result = 0
for stone in stones:
    if stone == 1:
        left += 1
        right -= 1
        if right < 0:
            right = 0
    elif stone == 2:
        left -= 1
        right += 1
        if left < 0:
            left = 0
    result = max(result, left, right)
print(result)

# now = stones[0]
# cnt = 1
# result = []
# for i in range(1, n):
#     if now != stones[i]:
#         result.append(cnt)
#         cnt = 1
#         now = stones[i]
#         continue
#     cnt += 1
# if cnt != 1:
#     result.append(cnt)

# temp = 0
# temp_lst = []
# for i in range(len(result)):
#     if i%2 == 0:
#         temp += result[i]
#         temp_lst.append(temp)
#     else:
#         temp -= result[i]
#         if temp < 0:
#             temp = 0
# temp2 = 0
# for i in range(len(result)):
#     if i%2 == 1:
#         temp2 += result[i]
#         temp_lst.append(temp2)
#     else:
#         temp2 -= result[i]
#         if temp2 < 0:
#             temp2 = 0
# print(max(temp_lst))