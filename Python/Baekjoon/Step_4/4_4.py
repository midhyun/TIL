st = []
for i in range(10):
    n = int(input())
    st.append(n % 42)
st = list(set(st))
print(len(st))