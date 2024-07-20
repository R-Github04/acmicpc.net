cli = []
for _ in range(3) : 
    li = [i for i in map(int, input().split())]
    cli.append(li.count(0))

for c in cli : 
    if c == 1 : print("A")
    if c == 2 : print("B")
    if c == 3 : print("C")
    if c == 4 : print("D")
    if c == 0 : print("E")