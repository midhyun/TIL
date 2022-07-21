# T = test_case
# k, n = floor, room_num
T= int(input())
for test_case in range(1,T+1):
    k = int(input())
    n = int(input())
    apt = [[man for man in range(1,n+1)]]

    for j in range(1,k+1):
        j_floor = []
        for i in range(1,n+1):
            num = sum(apt[j-1][:i])
            j_floor.append(num)
        apt.append(j_floor)
    print(apt[k][n-1])