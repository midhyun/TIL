import sys
sys.stdin = open('2857.txt')
input = sys.stdin.readline
check = False
for i in range(5):
    name = input().strip()
    if 'FBI' in name:
        print(i+1)
        check = True
if check == False:
    print('HE GOT AWAY!')
