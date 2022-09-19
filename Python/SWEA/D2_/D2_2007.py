import sys
sys.stdin = open('D2_2007.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1,t+1):
    sentence = input().strip()
    result = ''
    for i in range(1,11):
        if sentence[:i] == sentence[i:i+i]:
            result = sentence[:i]
            break
    print(f'#{test_case} {len(result)}')