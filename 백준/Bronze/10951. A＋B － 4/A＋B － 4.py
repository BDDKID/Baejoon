import sys

while True:
    try:
        A,B = map(int,sys.stdin.readline().split())
        S=A+B
        print(S)
    except:
        break