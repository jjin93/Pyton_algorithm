import sys
T = int(sys.stdin.readline())
for i in range(T):
    # str타입으로 입력받는다
    R,word = map(str,sys.stdin.readline().split())
    # str 타입의 word의 한문자한문자마다 포문이 돈다
    # 여기서 j는 해당 위치의 문자이다.
    for j in word:
        print(j*int(R),end='')

    print()    
   
