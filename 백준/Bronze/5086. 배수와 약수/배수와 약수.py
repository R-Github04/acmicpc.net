li = []
while 1 :
    a, b = map(int, input().split())
    if a == 0 and b == 0 : break
    
    if b%a == 0 : 
        li.append("factor")
    elif a%b == 0 : 
        li.append("multiple")
    else : 
        li.append("neither")
    
for i in li : 
    print(i)