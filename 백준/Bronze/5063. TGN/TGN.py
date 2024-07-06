li = []
t = int(input())
for i in range(t) : 
    r, e, c = map(int, input().split())
    if r < e - c : li.append("advertise")
    elif r == e - c : li.append("does not matter")
    elif r > e - c : li.append("do not advertise")
for i in li : 
    print(i)