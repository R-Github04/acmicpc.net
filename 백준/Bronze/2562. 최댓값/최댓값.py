li = []
for _ in range(9) : 
    li.append(int(input()))

for i in li : 
    if i == max(li) : 
        print(i)
        print(li.index(i) + 1)