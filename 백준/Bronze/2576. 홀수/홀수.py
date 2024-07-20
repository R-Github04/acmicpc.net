li = []
for i in range(7) : 
    i = int(input())
    if i % 2 == 1 : li.append(i)

if not len(li) : 
    print(-1)
else : 
    print(sum(li))
    print(sorted(li)[0])