d = input()
r = 10
for i in range(len(d) - 1) : 
    if d[i] == d[i+1] : 
        r += 5
    else : 
        r += 10
print(r)