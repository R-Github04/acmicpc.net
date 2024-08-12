n, m = map(int, input().split())
listA = []
listB = []
for i in range(n) : 
    listA.append(list(map(int, input().split())))
for i in range(n) : 
    listB.append(list(map(int, input().split())))


li = list(zip(listA, listB))

result = []
for i in li : 
    temp = []
    for m_ in range(m) :
        temp.append(i[0][m_]+i[1][m_])
    result.append(temp)

print('\n'.join([' '.join([str(j) for j in i]) for i in result]))