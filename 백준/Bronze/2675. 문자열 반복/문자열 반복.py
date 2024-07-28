st = ""
li = []
for i in range(int(input())) :
    st = ""
    a, b = input().split(); a = int(a)
    for b_ in b :
        st += b_ * a
    li.append(st)
for i in li :
    print(i)