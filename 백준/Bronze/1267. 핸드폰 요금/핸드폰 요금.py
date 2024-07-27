n = int(input())
li = []
for i in map(int, input().split()) : 
    li.append(i)
    
y, m = 0, 0
for i in li :
    yc, mc = 1, 1
    # case Y 
    yc += int(i / 30)
    #print("yc :", yc)
    # case M
    mc += int(i / 60)
    #print("mc :", mc)
    y += yc
    m += mc

y = y * 10
m = m * 15

#print("y :", y)
#print("m :", m)

if y == m : 
    print("Y M", y)
elif y < m : 
    print("Y", y)
elif m < y : 
    print("M", m)