import sys
# 함수 만들기
def boundary_x(x,w):
    if (w-x) > x :
        result1=x
        return result1
    else :
        result1 = w-x
        return result1
def boundary_y(h,y) :       
    if (h-y) > y :
        result2=y
        return result2
    else :
        result2 = h-y
        return result2            


# 입력 4개 한줄로 받기
x,y,w,h = map(int,sys.stdin.readline().split())
a =boundary_x(x,w)
b =boundary_y(h,y)

if a>b :
    print(b)
else :
    print(a)    
 