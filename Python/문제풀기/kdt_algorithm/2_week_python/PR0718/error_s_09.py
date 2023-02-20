# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)

# fruit_count = {furit: 1} 을 사용하면서 딕셔너리의 값이 
# for문이 반복될 때마다 {furit : 1} 로 덮어씌워지면서 이전의 값이 사라짐

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 딕셔너리에 키-값 쌍을 추가하는 명령어는
# dict[키] = 값 이다.
# 리스트에 값을 추가하는 명령어는
# list.append(값) 이다.