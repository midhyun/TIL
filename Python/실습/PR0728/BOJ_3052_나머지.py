remains = []
for i in range(10):                     # 10번 순회
    remains.append(int(input()) % 42)   # 입력받은 값을 42로 나눈 나머지를 리스트에 추가
print(len(list(set(remains))))
