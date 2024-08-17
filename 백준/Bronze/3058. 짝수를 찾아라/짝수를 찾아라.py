t = int(input())
for _ in range(t) : 
    li = [i for i in map(int, input().split())]
    c = 0
    min_num = 101
    for i in li : 
        if i % 2 == 0 : 
            c += i
            min_num = min(i, min_num)
    print(c, min_num)
    
        
    