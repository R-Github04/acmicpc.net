li = []
while 1 : 
    a, b = map(int, input().split())
    if a == b == 0 : 
        for i in li :
            print(i)
        break
    if a > b : li.append("Yes")
    else : li.append("No")