import sys
sys.stdin = open('2948_문자열교집합.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    cnt = 0
    temp = 0
    n, m = map(int, input().split())
    word1 = sorted(input().strip().split())
    word2 = sorted(input().strip().split())
    for a in word1:
        for b in range(temp, m):
            if a == word2[b]:
                cnt += 1
                temp = b
                break
            elif a < word2[b]:
                temp = b
                break
    print(f'#{test_case}', cnt)