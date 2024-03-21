import sys
sys.stdin = open('16719_ZOAC.txt')
input = sys.stdin.readline

def solution(str):
    if len(str) == 1:
        print(str)
        return
    for i in range(len(str)-1):
        if str[i] <= str[i+1]:
            continue
        else:
            nxt_str = str[:i] + str[i+1:]
            break
    else:
        nxt_str = str[:-1]
    
    solution(nxt_str)
    print(str)

solution(input().rstrip())