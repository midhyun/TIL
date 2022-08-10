# 소의 위치 N번 관찰
# 각 관찰은 소의 번호, 소의 위치
# 소 10마리 있음
# 길의 왼쪽 0 , 오른쪽 1
# 소가 최소 몇번 길을 건넜는지 /
cow_dict = {3:0}
N = int(input())
cow_num, position = map(int, input().split())
cow_dict[cow_num] = cow_dict.get(cow_num, position)

print(cow_dict)