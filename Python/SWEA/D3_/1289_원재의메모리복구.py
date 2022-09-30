import sys
sys.stdin = open('1289_원재의메모리복구.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    memory = input().strip()
    check = False
    cnt = 0
    for mem in memory:
        if mem == '0' and check:
            cnt += 1
            check = not check
        elif mem == '1' and not check:
            cnt += 1
            check = not check
    print(f'#{test_case} {cnt}')