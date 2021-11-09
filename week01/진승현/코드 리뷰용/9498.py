import sys
def score(x):
    if 90 <= x <= 100 :
        print('A')
    elif 80 <= x <90 :
        print('B')
    elif 70 <= x <80 :
        print('C')
    elif 60 <= x <70 :
        print('D')
    else :
        print('F')        
a=int(sys.stdin.readline())
score(a)

# 입력과 함수 중 어느것을 먼저 순서로 읽히는지 알아보자.
        
