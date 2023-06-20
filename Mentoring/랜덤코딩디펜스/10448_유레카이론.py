import sys
sys.stdin = open('10448_유레카이론.txt')
input = sys.stdin.readline

TESTCASE = int(input())
nums = []
tn = []
for _ in range(TESTCASE):
    nums.append(int(input()))

for i in range(1, 45):
    tn.append(i*(i+1)/2)

def find(x):
    for i in range(44):
        for j in range(44):
            for k in range(44):
                if tn[i] + tn[j] + tn[k] == x:
                    return 1

    return 0

for num in nums:
    print(find(num))