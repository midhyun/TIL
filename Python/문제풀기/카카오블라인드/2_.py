n = 7
cap = 2
deliveries = [1,0,2,0,1,0,2]
pickups = [0,2,0,1,0,2,0]
# 뒤집힌 리스트
deliveries_r = deliveries[::-1]
pickups_r = pickups[::-1]
answer = 0
start = 0

exit = 0
while True:
    for i in range(start,n):
        if deliveries_r[i] != 0 or pickups_r[i] != 0:
            start = i
            break
    now_d = cap
    now_p = cap

    for i in range(start,n):
        if deliveries_r[i] < now_d:
            now_d -= deliveries_r[i]
            deliveries_r[i] = 0
        elif now_d != 0 and deliveries_r[i] >= now_d:
            deliveries_r[i] -= now_d
            now_d = 0
        if pickups_r[i] < now_p :
            now_p -= pickups_r[i]
            pickups_r[i] = 0
        elif now_p != 0 and pickups_r[i] >= now_p:
            pickups_r[i] -= now_p
            now_p = 0
        if now_d == 0 and now_p == 0:
            break
    if now_d == cap and now_p == cap:
        break
    answer += (n - start)*2
print(answer)