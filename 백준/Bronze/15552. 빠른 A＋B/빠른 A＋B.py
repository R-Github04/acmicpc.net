from sys import stdout, stdin
t = int(stdin.readline().rstrip())

for _ in range(t) : 
    a, b = map(int, stdin.readline().rstrip().split())
    stdout.write(str(a + b)+"\n")