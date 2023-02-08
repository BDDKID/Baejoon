x, y, w, h = map(int,input().split())
X = w - x
Y = h - y
print(min(x,y,X,Y))