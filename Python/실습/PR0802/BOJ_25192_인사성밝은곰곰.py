import sys
import heapq
sys.stdin = open('25192.txt')
input = sys.stdin.readline
N = int(input())
chat_lst = [input().strip() for i in range(N)]  # for i in range(N):                    # 채팅 로그를 리스트 컴프리헨션으로 담아줌
chat_dic = {}                                   #     chat_lst.append(input().strip())  
say_hi = set()
cnt = 0
print(chat_lst)


for i in chat_lst:
    if i == 'ENTER':
        say_hi.clear()
    elif i in say_hi:
        chat_dic[i] = chat_dic.get(i, 0) + 1
    else:
        say_hi.add(i)
        cnt += 1
print(cnt)