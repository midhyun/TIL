import sys
sys.stdin = open('15989_1, 2, 3 더하기 4.txt')
input = sys.stdin.readline

def solution():
    test_case = int(input())
    dp = [0] * 10001
    dp[1], dp[2], dp[3] = 1, 2, 3
    numbers = []

    for i in range(test_case):
        numbers.append(int(input()))
    
    for i in range(4, max(numbers) + 1):
        if i % 2 == 0:
            cnt_2 = i // 2
            temp = 1 + cnt_2 // 3
        else:
            cnt_2 = (i-3) // 2
            temp = 1 + cnt_2 // 3

        dp[i] = dp[i - 1] + temp
    
    for number in numbers:
        print(dp[number])

solution()
