import sys
from collections import defaultdict
from datetime import datetime
sys.stdin = open('21942_부품 대여장.txt')
input = sys.stdin.readline

def get_datetime(date, time):
    year, month, day = map(int, date.split("-"))
    hour, minute = map(int, time.split(":"))
    return datetime(year, month, day, hour, minute)

N, L, F = input().split()
N, F = int(N), int(F)

rent_day, rent_time = L.split('/')
rent_hour, rent_min = map(int, rent_time.split(':'))
rent_time = (int(rent_day)*1440) + (int(rent_hour)*60) + rent_min

rent = defaultdict()
fee = defaultdict(int)

for _ in range(N):
    date, time, item, user = input().split()
    rent_value = get_datetime(date, time)

    if user not in rent:
        rent[user] = {}
    
    if item in rent[user]:
        start_datetime = rent[user].pop(item)
        diff_datetime = rent_value - start_datetime
        diff_min = (diff_datetime.days * 1440) + (diff_datetime.seconds // 60)
        if diff_min > rent_time:
            fee[user] = fee.get(user, 0) + (diff_min - rent_time) * F
    else:
        rent[user][item] = rent_value

if fee.keys():
    for key in sorted(fee.keys()):
        print(key, end=" ")
        print(fee.get(key))
else:
    print(-1)