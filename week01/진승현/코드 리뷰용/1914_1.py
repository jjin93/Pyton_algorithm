import sys
def move(no: int, x:int, y:int) -> None:
    if no > 1 :
        move(no - 1, x, 6 - x - y)
    print(x, y)

    if no > 1:
        move(no - 1, 6 - x - y, y)
n = int(sys.stdin.readline())
print((2**n)-1)
if(n <= 20):
    move(n,1,3)
else:
    (2**n)-1            
    

    # 313 212 113 1-3 1-2 132 3-2 1-3 223 121 2-1 2-3 113 1-3 /
