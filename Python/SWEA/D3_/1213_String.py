import sys
sys.stdin = open('1213_String.txt')
input = sys.stdin.readline

for test_case in range(1, 11):
    n = int(input())
    moonja = input().strip()
    moonja_line = input().strip()
    print(f"#{test_case} {moonja_line.replace(moonja,'#').count('#')}")
