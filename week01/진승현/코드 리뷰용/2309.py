import sys
x = [0]*9
for i in range(9):
    ki = int(sys.stdin.readline())
    x[i] = ki


total = sum(x)


for i in range(9):
    for j in range(i+1,9):
        if total -x[i] - x[j] == 100:
            a= x[i]
            b= x[j]
            break

x.remove(a)
x.remove(b)
x = sorted(x)
for i in range(len(x)):
    print(x[i])
