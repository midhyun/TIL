kap_lst = []

def kapka(n):
    result = n
    for i in str(n):
        result += int(i)
    return result
# n의 카프카 함수값 
for i in range(10000): # 1부터 카프카 값을 추가
    kap_lst.append(kapka(i))
    if i not in kap_lst: # 카프카 값은 n보다 무조건 크다.
        print(i)
