import sys
T = int(sys.stdin.readline())
result = []

for count in range(0,T):
     a,b = map(int,sys.stdin.readline().split())
     x = (a+b)
     result.append(x)
   
for count in range(0,T) :
    print(result[count])   