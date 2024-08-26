import math

m = int(input())
n = int(input())
li = []
if (not m % math.sqrt(m)) == 0 : 
    for i in range (int(math.sqrt(m)) + 1, int(math.sqrt(n)) + 1) : 
        li.append(i**2)
else : 
    for i in range (int(math.sqrt(m)), int(math.sqrt(n)) + 1) : 
        li.append(i**2)
        
if len(li) == 0 : print(-1)
else : 
    print(sum(li))
    print(li[0])
