import sys
sys.stdin = open('20291_파일정리.txt')
input = sys.stdin.readline

N = int(input())

def organize(n):
    dic = {}

    for _ in range(n):
        filename = input().rstrip().split('.')
        
        dic[filename[1]] = dic.get(filename[1], 0) + 1
    
    for extension, cnt in sorted(list(dic.items())):
        print(extension, cnt)

organize(N)