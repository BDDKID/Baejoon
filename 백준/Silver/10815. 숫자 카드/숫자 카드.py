import sys
input = sys.stdin.readline

N = int(input())
my_card = set(map(int,input().split()))
M = int(input())
given_card = list(map(int,input().split()))


for i in given_card:
    if i in my_card:
        print(1,end=" ")
    else:
        print(0,end=" ")