t = int(input())
li = []

while t : 
    ra, rb = 0, 0
    for _ in range(9) : 
        a, b = map(int, input().split())
        ra += a
        rb += b
    if ra > rb : li.append("Yonsei")
    elif ra < rb : li.append("Korea")
    else : li.append("Draw")
    
    t -= 1

for i in li : print(i)