import sys
sys.stdin = open('7453_합이0인네정수.txt')
input = sys.stdin.readline

# 정수로 이루어진 크기가 같은 배열 4개가 있다.
# 각 배열에서 하나씩 꺼낸 합이 0인 (a, b, c, d) 경우의 수는?
# def solution():
#     N = int(input())
#     # 배열 A, B, C, D
#     A, B, C, D = [], [], [], []
#     for _ in range(N):
#         a, b, c, d = map(int, input().split())
#         A.append(a); B.append(b); C.append(c); D.append(d)

#     front_list, back_list = [], []
#     # front_dict, back_dict = defaultdict(int), defaultdict(int)

#     for i in range(N):
#         for j in range(N):
#             front_list.append((A[i]+B[j]))
#             back_list.append((C[i]+D[j]))
#             # front_dict[A[i]+B[j]] += 1
#             # back_dict[C[i]+D[j]] += 1

#     front_list.sort(); back_list.sort()

#     s, e = 0, len(back_list)-1

#     result = 0
#     while s < len(front_list) and e >= 0:
#         if front_list[s] + back_list[e] == 0:
#             nxt_s, nxt_e = s + 1, e - 1
#             while nxt_s < len(front_list):
#                 if front_list[s] != front_list[nxt_s]:
#                     break
#                 nxt_s += 1
#             while nxt_e >= 0:
#                 if back_list[e] != back_list[nxt_e]:
#                     break
#                 nxt_e -= 1
#             result += (nxt_s-s) * (e-nxt_e)
#             s = nxt_s; e = nxt_e
#         elif front_list[s] + back_list[e] > 0:
#             e -= 1
#         else:
#             s += 1

#     print(result)

# solution()

def solution():
    n = int(input())
    A, B, C, D = [], [], [], []
    result = 0

    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a); B.append(b); C.append(c); D.append(d)

    ab_dict = {}
    for a in A:
        for b in B:
            tmp = a + b
            ab_dict[tmp] = ab_dict.get(tmp, 0) + 1

    for c in C:
        for d in D:
            tmp = -(c+d)
            if tmp in ab_dict:
                result += ab_dict[tmp]
    
    print(result)


solution()