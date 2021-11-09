import sys
def leap_year(x):
    if (x%4) == 0 and (x%100) != 0 or (x%400) == 0 :
       print('1')
    else :
        print('0')

a = int(sys.stdin.readline())
leap_year(a)
# or로 묶을 때 괄호처리를 해줘야하는지