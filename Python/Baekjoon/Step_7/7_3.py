A, B, V = map(int,input().split())
day = (V - A) // (A - B)

print(day+1) if  (V - A) % (A - B) == 0 else print(day+2) 
