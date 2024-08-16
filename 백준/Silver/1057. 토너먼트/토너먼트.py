n, kim, lim = map(int, input().split())
round = 1

while n+1 > 2**round : 
    if ((kim % 2 == 0) and (kim - 1 == lim)) or ((lim % 2 == 0) and (lim - 1 == kim)) : 
        print(round)
        break
    else : 
        round += 1
        kim = (kim + 1) // 2
        lim = (lim + 1) // 2
    #print(round, kim, lim)
    
    if n+1 <= 2**round :
        print(round)