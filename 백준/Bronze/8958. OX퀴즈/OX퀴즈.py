n = int(input())
li = []
r = 0
for n_ in range(n) : 
    in_s = input().split("X")
    for i in in_s : 
        if len(i) != 0 : 
            r += int(len(i) * (1 + len(i)) / 2)
    li.append(r)
    r = 0
    
for i in li : 
    print(i)