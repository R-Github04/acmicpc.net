n = int(input())
li = []
for i in map(int, input().split()) : 
    li.append(i)
    
y, m = 0, 0
for i in li :
    yc, mc = 1, 1
    
    yc += int(i / 30)
    mc += int(i / 60)
    
    y += yc
    m += mc

y = y * 10
m = m * 15

if y == m : 
    print("Y M", y)
elif y < m : 
    print("Y", y)
elif m < y : 
    print("M", m)