def findP(n) : 
    li = []
    for i in range(n - 1) :
        if n % (i+1) == 0 : li.append(i+1)

    if sum(li) == n :
        print(n, "= ", end = "")
        for i in li[:-1] : 
            print(i, "+ ", end="")
        print(li[-1])
    else : print(n, "is NOT perfect.")

nli = []
while 1 : 
    nli.append(int(input()))
    if nli[-1] == -1 : break
for n in nli[:-1] : 
    findP(n)