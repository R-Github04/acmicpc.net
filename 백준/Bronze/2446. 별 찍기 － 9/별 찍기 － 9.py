n = int(input())
t = n
c = 0


while 1 : 
    for i in range(c) : 
        print(" ", end = "")        
    for i in range(2 * t - 1) : 
        print("*", end = "")
    if c >= n - 1 : 
        break
    print()
    t -= 1
    c += 1
while 1 : 
    if c != n - 1 : 
        for i in range(c) : 
            print(" ", end = "")    
    if (2 * t - 1) != 1 :
        for i in range(2 * t - 1) : 
            print("*", end = "")
    if c <= 0 : 
        break
    print()
    t += 1
    c -= 1
    