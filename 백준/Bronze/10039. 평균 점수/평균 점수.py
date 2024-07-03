li = []
for i in range(5) : 
    n = int(input())
    if n > 40 : li.append(n)
    else : li.append(40)
print(int(sum(li)/5))
