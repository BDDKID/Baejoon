import sys

while True:
    A,B = map(int,sys.stdin.readline().split())
    S=A+B
    if S==0:
        break
    else:
        print(S)