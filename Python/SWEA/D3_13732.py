import sys
sys.stdin = open('input.txt','r')


N = int(input())
n_lst = []
for i in range(N):
    a = input()
    m_lst = []
    for j in a:
        m_lst.append(j)
    n_lst.append(m_lst)

print(n_lst)