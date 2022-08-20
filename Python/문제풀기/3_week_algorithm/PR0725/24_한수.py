N = int(input())
cnt = 0

for i in range(1, N+1): # N 까지의 숫자를 하나씩 넣어줌
    num = str(i) # 숫자를 문자열로 변환
    if i < 100: # 100미만의 숫자는 모두 한수임.
        cnt += 1
    else:
        long = 0
        for j in range(1,len(num)): # 십의 자릿수부터 이전자릿수와의 차이를 1의자리와 10의 자릿수의 차이와 비교함
            
                long += 1 if (int(num[j]) - int(num[j-1])) == (int(num[1]) - int(num[0])):
        if long == len(num)-1: # 4자릿수일경우 각 자릿수의 차이가 같은 3번의 경우가 있으면 한수임.
            cnt += 1 # 등차수열이면 카운트
        
print(cnt)
a,b,c,d = map(int, num[j],num[j-1],num[1],num[0])
