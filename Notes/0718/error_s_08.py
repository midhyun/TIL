# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# count += 1 행의 들여쓰기가 맞지 않아 생기는 오류.
# total을 count로 나눈 몫을 나타내는 //를 사용해서 5가나옴
# /로 바꾸어주면 나눈 값이나옴.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)