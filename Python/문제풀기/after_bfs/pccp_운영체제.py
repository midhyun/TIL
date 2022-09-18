import sys
import heapq

program = [[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]
s_prg = []
answer = [0]*11
wait = []
cur = 0
for i in program:
    prior, call_t, run_t = i
    heapq.heappush(s_prg, (call_t, prior, run_t))
call_t, prior, run_t = heapq.heappop(s_prg)
cur += call_t + run_t
for _ in range(len(s_prg)):
    for _ in range(len(s_prg)):
        call_t, prior, run_t = heapq.heappop(s_prg)
        if call_t > cur:
            heapq.heappush(s_prg, (call_t, prior, run_t))
            break
        heapq.heappush(wait, (prior, call_t, run_t))
    if len(wait) == 0:
        call_t, prior, run_t = heapq.heappop(s_prg)
        cur = call_t + run_t
        continue
    prior, call_t, run_t = heapq.heappop(wait)
    if call_t < cur:
            answer[prior] += (cur-call_t)
    cur += run_t

answer[0] = cur
print(answer)