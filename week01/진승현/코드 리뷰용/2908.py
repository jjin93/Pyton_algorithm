import sys
a,b = map(int,sys.stdin.readline().split())
a = str(a)
b = str(b)
a_reverse =''
b_reverse =''
for i in a:
    a_reverse = i + a_reverse
    # a 가 478 이면 4 -> 74 -> 874 순으로 된다.

for i in b:
    b_reverse = i + b_reverse    

a_reverse = int(a_reverse)
b_reverse = int(b_reverse)
if(a_reverse > b_reverse):
    print(a_reverse)
else :
    print(b_reverse)        



