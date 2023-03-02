C = int(input())

for i in range(C):
    cnt = 0
    score = list(map(int,input().split()))
    mean = (sum(score)-score[0])/score[0] 
    for j in score[1:] :
        if mean < j :
            cnt +=1
    
    rating = cnt/score[0]*100
    print(f'{rating:.3f}%')