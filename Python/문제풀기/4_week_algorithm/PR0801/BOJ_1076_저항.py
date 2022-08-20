from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

line_1 = input().strip()
line_2 = input().strip()
line_3 = input().strip()
dic_num = {
    'black':0,
    'brown':1,
    'red':2,
    'orange':3,
    'yellow':4,	
    'green':5,
    'blue':6,	
    'violet':7,
    'grey':8,
    'white':9,
}
dic_mul = {
    'black':1,
    'brown':10,
    'red':1e2,
    'orange':1e3,
    'yellow':1e4,	
    'green':1e5,
    'blue':1e6,	
    'violet':1e7,
    'grey':1e8,
    'white':1e9,
}

result = (dic_num[line_1]*10 + dic_num[line_2]) * dic_mul[line_3]
print(int(result))