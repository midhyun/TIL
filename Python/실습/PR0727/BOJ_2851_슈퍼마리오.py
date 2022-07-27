import sys
sys.stdin = open('input.txt')

score_lst = []
for i in range(10):
    score_lst.append(int(input()))
result = score_lst[0]
if sum(score_lst) < 100:
    print(sum(score_lst))
else:
    for score in score_lst[1:]:
        b_result = result
        result += score
        if abs(b_result-100) > abs(result-100):
            pass
        elif abs(b_result-100) == abs(result-100):
            print(result)
            break
        elif abs(b_result-100) < abs(result-100):
            print(b_result)
            break
    else: print(result)

# ans, score = 0, 0
# for i in range(10):
#     score += int(input())
#     if 100-ans >= abs(100-score):
#         ans=score
# print(ans)
