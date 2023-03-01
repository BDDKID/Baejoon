import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S_ls = []

for i in range(N):
    ch2  = input()
    S_ls.append(ch2)


S_set = set(S_ls)


cnt = 0

for i in range(M):
    ch2 = input()
    if ch2 in S_set:
        cnt += 1
    else: continue

print(cnt)