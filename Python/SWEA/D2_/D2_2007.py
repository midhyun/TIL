import sys
sys.stdin = open('D2_2007.txt')
input = sys.stdin.readline

# t = int(input())
# for test_case in range(1,t+1):
#     sentence = input().strip()
#     result = ''
#     for i in range(1,11):
#         if sentence[:i] == sentence[i:i+i]:
#             result = sentence[:i]
#             break
#     print(f'#{test_case} {len(result)}')
T = int(input())

for tc in range(1,T+1):
  str = input() 
  j = 0 # 시작값과 비교해야하기 때문에

  for i in range(1, len(str)): #
    if str[i] == str[j]: #
      j += 1
    else:
      j = 0

  print(f"#{tc} {len(str)-j}")