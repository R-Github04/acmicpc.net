v = int(input())
o = input()
a = v
for i in o : 
    if i == "B" : 
        a -= 1
b = v - a
if a > b : print("A")
elif a < b : print("B")
else : print("Tie")