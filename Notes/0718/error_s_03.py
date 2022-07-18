# numbers = input().split()
# print(sum(numbers))
# input은 str로 받았는데 sum은 int로 가능함.

numbers = map(int,input().split())
print(sum(numbers))