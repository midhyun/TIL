import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    password_len = int(input())                 # 11
    password = input().split()                  # lst
    order_insert_cnt = int(input())             # 7
    order_inserts = input().split('I')          # lst

    for i in range(1, order_insert_cnt + 1):
        insert = order_inserts[i].split()       # insert[0] == idx, insert[1] == len(insert)
        password = password[:int(insert[0])] + insert[2:] + password[int(insert[0]):]
    
    print(f'#{test_case}', end = ' ')
    for i in range(10):
        print(password[i], end = ' ')
    print()