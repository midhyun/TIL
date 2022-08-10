import sys
sys.stdin = open('10769.txt')
input = sys.stdin.readline

# 행복 = ':-)' 슬픔 = ':-('
# 이모티콘 없으면 none
# 행복과 슬픔의 숫자가 같으면 unsure
# 행복이 더 많으면 happy
# 슬픔이 더 많으면 sad

message_ = input().strip()

happy = message_.count(':-)')
sad = message_.count(':-(')

if happy > sad:
    print('happy')
elif sad > happy:
    print('sad')
elif sad == 0 and happy == 0:
    print('none')
elif sad == happy:
    print('unsure')
