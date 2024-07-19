rli = []
c = 0
while 1 : 
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x2-x1) : 
        for y in range(y2-y1) : 
             if not (x1 + x, y1 + y) in rli : rli.append((x1 + x, y1 + y))
    c += 1
    if c == 4 : 
        print(len(rli))
        break