N = int(input())
n = list(map(int,input().split()))
cnt = 0
for i in n:
    mixed = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                mixed += 1
        if mixed == 0:
            cnt += 1
print(cnt)