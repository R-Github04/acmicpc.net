ali = list(input())
bli = list(input())
c = 0
for i in range(26) : 
    c += abs(ali.count(chr(97+i)) - bli.count(chr(97+i)))
print(c)