import sys
sys.stdin = open('5875_오타.txt')
input = sys.stdin.readline

# 올바른 괄호쌍을 좋아하는 키파는 최근에 노트북을 샀다. 
# 그런데 키보드의 크기가 너무 작았기 때문에, 키파는 혹시 여는 괄호와 닫는 괄호를 서로 잘못 입력하지 않았는지 걱정되었다. 
# 키파를 도와 올바른 괄호쌍이 되도록 고쳐 주자 
# 키파는 괄호를 입력할 때 매우 조심했기 때문에 최대 한 번 오타를 내었다. 올바른 괄호쌍은 다음과 같이 정의된다.
# - ()는 올바른 괄호쌍이다.
# - A가 올바른 괄호쌍이라면 (A) 또한 올바른 괄호쌍이다.
# - A와 B가 올바른 괄호쌍이라면 AB 또한 올바른 괄호쌍이다.
# ()(())))
insert = input().rstrip()
stack = []
point = []
for i in range(len(insert)):
    if insert[i] == '(':
        stack.append((insert[i], i))
    elif stack and insert[i] == ')':
        stack.pop()
    elif not stack and insert[i] == ')':
        point.append((insert[i], i))
if not point:
    point = stack

if point and point[0][0] == ')':
    result = insert[:point[0][1]+1].count(')')
elif point and point[-1][0] == '(':
    result = insert[point[-1][1]:].count('(')
else:
    result = 0

print(result)