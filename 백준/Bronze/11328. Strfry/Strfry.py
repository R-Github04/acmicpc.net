n = int(input())
for _ in range(n) : 
    c = 0
    s1, s2 = map(list, input().split())
    for i in range(26) : 
        c += abs(s1.count(chr(97+i)) - s2.count(chr(97+i)))
    if c == 0 : 
        print("Possible")
    else : 
        print("Impossible")