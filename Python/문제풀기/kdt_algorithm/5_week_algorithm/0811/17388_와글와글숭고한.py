import sys
sys.stdin = open('17388.txt')
input = sys.stdin.readline

S, K, H = map(int, input().split())
sum_ = sum([S,K,H])
parti = {'Soongsil': S, 'Korea': K, 'Hanyang': H}
if sum_ >= 100:
    print('OK')
else:
    for k, v in parti.items():
        if v == min([S,K,H]):
            print(k)